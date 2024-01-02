from rest_framework.routers import DefaultRouter



from .viewsets import ProductViewSet

router = DefaultRouter()
router.register(
   'product-views',
    ProductViewSet,
    basename="product-v2-views"
)

urlpatterns = router.urls