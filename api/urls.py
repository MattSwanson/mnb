from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'bags', views.BagViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'item_revisions', views.ItemRevisionViewSet)
router.register(r'finishes', views.FinishViewSet)
router.register(r'parts', views.PartViewSet)
router.register(r'kits', views.KitViewSet)
router.register(r'boxes', views.BoxViewSet)
router.register(r'kitparts', views.KitpartViewSet)
router.register(r'uoms', views.UomViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
