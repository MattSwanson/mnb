from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'bags', views.BagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
