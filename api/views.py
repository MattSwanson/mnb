from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import viewsets

from api.models import Bag
from api.serializers import BagSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return response({
        'bags': reverse('bag-list', request=request, format=format),
    })

class BagViewSet(viewsets.ModelViewSet):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer


def index(request):
    return HttpResponse("This is the beginning...")


