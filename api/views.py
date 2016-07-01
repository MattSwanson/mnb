from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

from api.models import *
from api.serializers import *

    

class BagViewSet(viewsets.ModelViewSet):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRevisionViewSet(viewsets.ModelViewSet):
    queryset = ItemRevision.objects.all()
    serializer_class = ItemRevisionSerializer

class FinishViewSet(viewsets.ModelViewSet):
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer
