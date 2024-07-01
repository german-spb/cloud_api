from backend_api.views import UserViewSet, UploudFilesViewSet
from rest_framework.routers import DefaultRouter
from backend_api import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'uploudfiles', views.UploudFilesViewSet, basename='uploudfiles')
urlpatterns = router.urls