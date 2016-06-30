from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = ('size', 'mil', 'top')

class ItemSerializer(serializers.ModelSerializer):
    revisions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Item
        fields = ('item_number', 'pref_vendor', 'def_uom', 'live_inv', 'revisions')


class ItemRevisionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ItemRevision
        fields = ('item', 'name', 'eff_date', 'live_inv')
