import datetime

from django.core.cache import cache


def change_api_updated_at(sender=None, instance=None, *args, **kwargs):
    cache.set('product_api_updated_at_timestamp',
              datetime.datetime.utcnow(), 60*15)
