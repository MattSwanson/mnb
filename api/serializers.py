from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = ('size', 'mil', 'top')

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ('length', 'width', 'height')
class UomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uom
        fields = ('name', 'abbrv')


class FinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finish
        fields = ('id', 'name', 'description', 'level')

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('item_revision', 'partdesc', 'size', 'origin')

class ItemRevisionSerializer(serializers.ModelSerializer):
    item = serializers.StringRelatedField()
    part = PartSerializer(many=False, read_only=True)

    class Meta:
        model = ItemRevision
        fields = ('item', 'name', 'eff_date', 'live_inv', 'part')

class ItemSerializer(serializers.ModelSerializer):
    revisions = ItemRevisionSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('item_number', 'def_uom', 'revisions')



class KitpartSerializer(serializers.ModelSerializer):
    part_rev = ItemRevisionSerializer(many=False, read_only=True)
    partuom = serializers.StringRelatedField()
    class Meta:
        model = Kitpart
        fields = ('partqty', 'partuom', 'part_rev')

class KitSerializer(serializers.ModelSerializer):
    item_revision = ItemRevisionSerializer(many=False, read_only=True)
    bagtype = BagSerializer(many=False)
    boxtype = BoxSerializer(many=False)
    kitparts = KitpartSerializer(many=True, read_only=True)

    class Meta:
        model = Kit
        fields = ('kitname', 'bagtype', 'boxtype', 'ctnqty', 'kitparts', 'item_revision')
 
