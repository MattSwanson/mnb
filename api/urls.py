from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'bags', views.BagViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'item_revisions', views.ItemRevisionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
