from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import viewsets

from api.models import *
from api.serializers import *

@api_view(['GET'])
def api_root(request, format=None):
    return response({
        'bags': reverse('bag-list', request=request, format=format),
    })

class BagViewSet(viewsets.ModelViewSet):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRevisionViewSet(viewsets.ModelViewSet):
    queryset = ItemRevision.objects.all()
    serializer_class = ItemRevisionSerializer


