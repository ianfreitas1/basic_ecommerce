import datetime
from django.core.cache import cache
from django.utils.encoding import force_text
from rest_framework_extensions.key_constructor.constructors import (
    DefaultKeyConstructor
)
from rest_framework_extensions.key_constructor.bits import (
    KeyBitBase,
    RetrieveSqlQueryKeyBit,
    ListSqlQueryKeyBit,
    PaginationKeyBit
)


class UpdatedAtKeyBit(KeyBitBase):
    key = 'api_updated_at_timestamp'
    timeout = 60 * 15  # Default 15 minutes timeout

    def get_data(self, **kwargs):
        value = cache.get(self.key, None)
        if not value:
            value = datetime.datetime.utcnow()
            cache.set(self.key, value=value, timeout=self.timeout)
        return force_text(value)


class CustomObjectKeyConstructor(DefaultKeyConstructor):
    retrieve_sql = RetrieveSqlQueryKeyBit()
    updated_at = UpdatedAtKeyBit()


class CustomListKeyConstructor(DefaultKeyConstructor):
    list_sql = ListSqlQueryKeyBit()
    pagination = PaginationKeyBit()
    updated_at = UpdatedAtKeyBit()
