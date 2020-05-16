from rest_framework.routers import SimpleRouter

from .views import OrderViewSet, PayOrderViewSet

router = SimpleRouter()
router.register(r'orders', OrderViewSet)
router.register(r'orders/pay', PayOrderViewSet)
urlpatterns = router.urls
