from rest_framework.routers import SimpleRouter

from .views import ClientViewSet

router = SimpleRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [

]

urlpatterns += router.urls
