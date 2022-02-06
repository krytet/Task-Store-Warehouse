import asyncio

from aiohttp import ClientSession
from django.contrib import admin

from .models import Order


session = ClientSession()
loop = asyncio.get_event_loop()


# Create/Update orden on warehouse
async def create_update_order(data, url, is_created):
    if is_created:
        await session.post(url, data=data)
    else:
        await session.patch(url, data=data)


# Request to call a function create/update
async def call_create_order(data, url, is_created):
    task = asyncio.create_task(create_update_order(url, data, is_created))
    await asyncio.gather(task)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'warehouse', 'status')
    list_filter = ('warehouse', 'status', )
    search_fields = ('id', )

    def save_model(self, request, obj, form, change):
        obj.save()
        if not change:
            url = obj.warehouse.url + 'api/orders/'
            # It is possible to add additional data
            data = {
                'id': obj.id,
                'warehouse': obj.warehouse.id,
                'status': obj.status
            }
        else:
            # It is possible to change,since only the status is changing so far
            url = obj.warehouse.url + 'api/orders/' + str(obj.id) + '/'
            data = {
                'status': obj.status
            }
        loop.run_until_complete(call_create_order(url, data, not change))


admin.site.register(Order, OrderAdmin)
