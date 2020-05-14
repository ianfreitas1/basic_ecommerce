from rest_framework.routers import SimpleRouter

from .views import OrderViewSet

router = SimpleRouter()
router.register(r'orders', OrderViewSet)
urlpatterns = router.urls
