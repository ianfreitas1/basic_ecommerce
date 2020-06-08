from basic_ecommerce.utils.cache import (CustomListKeyConstructor,
                                         CustomObjectKeyConstructor,
                                         UpdatedAtKeyBit)


class ProductUpdatedAtKeyBit(UpdatedAtKeyBit):
    key = 'product_api_updated_at_timestamp'


class ProductObjectKeyConstructor(CustomObjectKeyConstructor):
    updated_at = ProductUpdatedAtKeyBit()


class ProductListKeyConstructor(CustomListKeyConstructor):
    updated_at = ProductUpdatedAtKeyBit()
