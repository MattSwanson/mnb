from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

from api.models import *
from api.serializers import *

    

class BagViewSet(viewsets.ModelViewSet):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class UomViewSet(viewsets.ModelViewSet):
    queryset = Uom.objects.all()
    serializer_class = UomSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRevisionViewSet(viewsets.ModelViewSet):
    queryset = ItemRevision.objects.all()
    serializer_class = ItemRevisionSerializer

class FinishViewSet(viewsets.ModelViewSet):
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class KitViewSet(viewsets.ModelViewSet):
    queryset = Kit.objects.all()
    serializer_class = KitSerializer

class KitpartViewSet(viewsets.ModelViewSet):
    queryset = Kitpart.objects.all()
    serializer_class = KitpartSerializer
