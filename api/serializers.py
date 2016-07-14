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
        fields = ('item_number', 'def_uom', 'revisions')

class FinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finish
        fields = ('id', 'name', 'description', 'level')

class PartSerializer(serializers.ModelSerializer):
    item_revision = ItemRevisionSerializer(many=False, read_only=True)

    class Meta:
        model = Part
        fields = ('item_revision', 'partdesc', 'size', 'origin')

class KitSerializer(serializers.ModelSerializer):
    item_revision = ItemRevisionSerializer(many=False, read_only=True)

    class Meta:
        model = Kit
        fields = ('kitname', 'bagtype', 'boxtype', 'ctnqty', 'item_revision')
