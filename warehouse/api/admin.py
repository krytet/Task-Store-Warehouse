import asyncio
import json
import os

from aiohttp import ClientSession
from django.contrib import admin
from dotenv import load_dotenv

from .models import Order


load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
url_store = f"{os.getenv('URL_TYPE')}://{os.getenv('URL_DOMEN')}/"
token = ''

session = ClientSession()
loop = asyncio.get_event_loop()


# Getting a token
async def get_token():
    response = await session.post(
        url_store + 'api/auth/token/login/',
        data={
            'username': username,
            'password': password
        }
    )
    return json.loads(await response.text())['auth_token']


# Update order
async def update_order(data, id, recursion=False):
    global token
    if not token:
        token = await get_token()
    response = await session.patch(
        url_store + f'api/orders/{id}/',
        data=data,
        headers={
            'Authorization': 'Token ' + token
        }
    )
    if response.status == 403:
        if not recursion:
            token = await get_token()
            await update_order(data, id, True)
        else:
            raise Exception("problems with authorization on server")


# Request to call a function create/update
async def call_update_order(data, id):
    task = asyncio.create_task(update_order(data, id))
    await asyncio.gather(task)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'warehouse', 'status')
    list_filter = ('status', )
    search_fields = ('id', )

    # Update order on store
    def save_model(self, request, obj, form, change):
        data = {
            'status': obj.status
        }
        loop.run_until_complete(call_update_order(data, obj.id))
        super().save_model(request, obj, form, change)


admin.site.register(Order, OrderAdmin)
