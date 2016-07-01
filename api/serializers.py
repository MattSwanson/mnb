from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = ('size', 'mil', 'top')

class ItemRevisionSerializer(serializers.ModelSerializer):
    item = serializers.StringRelatedField()

    class Meta:
        model = ItemRevision
        fields = ('item', 'name', 'eff_date', 'live_inv')

class ItemSerializer(serializers.ModelSerializer):
    revisions = ItemRevisionSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('item_number', 'pref_vendor', 'def_uom', 'live_inv', 'revisions')

class FinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finish
        fields = ('id', 'name', 'company', 'description', 'baseprice', 'level')
