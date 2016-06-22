# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Bags(models.Model):
    size = models.CharField(max_length=5)
    mil = models.IntegerField()
    top = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'Bags'


class Boxes(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Boxes'


class Partfinishes(models.Model):
    part = models.ForeignKey('Part', models.DO_NOTHING)
    finishid = models.ForeignKey('Finishes', models.DO_NOTHING, db_column='FinishId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PartFinishes'


class Addresses(models.Model):
    company = models.ForeignKey('Companies', models.DO_NOTHING)
    line_1 = models.CharField(max_length=50)
    line_2 = models.CharField(max_length=50)
    line_3 = models.CharField(max_length=50)
    line_4 = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'addresses'


class AppNews(models.Model):
    subject = models.CharField(max_length=25)
    body = models.CharField(max_length=100)
    date = models.DateTimeField()
    max_app_version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_news'


class AppVersions(models.Model):
    app_id = models.SmallIntegerField(primary_key=True)
    app_version_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_versions'


class Calendar(models.Model):
    datefield = models.DateField()
    year = models.SmallIntegerField()
    month = models.IntegerField()
    day_of_week = models.IntegerField()
    day_of_year = models.SmallIntegerField()
    day_of_month = models.IntegerField()
    week = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calendar'


class Changelog(models.Model):
    revision_id = models.IntegerField()
    note = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'changelog'


class CiSessions(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40)
    ip_address = models.CharField(max_length=45)
    last_activity = models.IntegerField()
    user_agent = models.CharField(max_length=120)
    user_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'ci_sessions'


class Companies(models.Model):
    name = models.CharField(max_length=50)
    vmi = models.IntegerField()
    homepage = models.CharField(db_column='homePage', max_length=50)  # Field name made lowercase.
    address = models.CharField(max_length=75, blank=True, null=True)
    phone = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'companies'


class Contacts(models.Model):
    company = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company')
    last = models.IntegerField()
    first = models.IntegerField()
    title = models.IntegerField()
    email = models.IntegerField()
    phone = models.IntegerField()
    fax = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contacts'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class FileCategories(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'file_categories'


class FileTypes(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'file_types'


class Files(models.Model):
    filecategory = models.ForeignKey(FileCategories, models.DO_NOTHING, db_column='fileCategory')  # Field name made lowercase.
    filetype = models.CharField(db_column='fileType', max_length=10)  # Field name made lowercase.
    views = models.IntegerField()
    addtime = models.DateTimeField(db_column='addTime')  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    origname = models.CharField(db_column='origName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    item_revision = models.ForeignKey('ItemRevision', models.DO_NOTHING, db_column='item_revision')

    class Meta:
        managed = False
        db_table = 'files'


class Finishes(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    company = models.IntegerField()
    description = models.TextField()
    baseprice = models.SmallIntegerField()
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finishes'


class InProcess(models.Model):
    po_id = models.IntegerField()
    new_po = models.ForeignKey('PurchaseOrders', models.DO_NOTHING)
    process = models.ForeignKey('Processes', models.DO_NOTHING)
    total_qty = models.IntegerField()
    uom = models.ForeignKey('Uom', models.DO_NOTHING, db_column='uom')
    complete = models.IntegerField()
    rec_date = models.DateField(blank=True, null=True)
    item_revision = models.ForeignKey('ItemRevision', models.DO_NOTHING, db_column='item_revision')

    class Meta:
        managed = False
        db_table = 'in_process'


class ItemAliases(models.Model):
    base_rev = models.ForeignKey('ItemRevision', models.DO_NOTHING, related_name='base_item_revision', db_column='base_rev')
    sub_rev = models.ForeignKey('ItemRevision', models.DO_NOTHING, related_name='sub_item_revision', db_column='sub_rev')

    class Meta:
        managed = False
        db_table = 'item_aliases'


class ItemReceiptTypes(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'item_receipt_types'


class ItemReceipts(models.Model):
    type = models.ForeignKey(ItemReceiptTypes, models.DO_NOTHING, db_column='type')
    rec_date = models.DateField()
    po_line = models.ForeignKey('PurchaseOrderLines', models.DO_NOTHING, blank=True, null=True)
    qty = models.IntegerField()
    uom = models.ForeignKey('Uom', models.DO_NOTHING, db_column='uom')
    proc_line = models.ForeignKey(InProcess, models.DO_NOTHING, blank=True, null=True)
    item_revision = models.ForeignKey('ItemRevision', models.DO_NOTHING, db_column='item_revision')

    class Meta:
        managed = False
        db_table = 'item_receipts'


class ItemReqLines(models.Model):
    report = models.ForeignKey('ItemReqs', models.DO_NOTHING)
    item_revision = models.ForeignKey('ItemRevision', models.DO_NOTHING, db_column='item_revision')
    qty = models.IntegerField()
    need_date = models.DateField()
    job = models.CharField(max_length=25)
    issued = models.IntegerField()
    whse = models.CharField(db_column='Whse', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_req_lines'


class ItemReqs(models.Model):
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'item_reqs'


class ItemRevision(models.Model):
    item = models.ForeignKey('Item', models.DO_NOTHING)
    name = models.CharField(max_length=10)
    eff_date = models.DateField()
    live_inv = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.item, self.name)

    class Meta:
        managed = False
        db_table = 'item_revisions'
        unique_together = (('item', 'name'),)


class ItemSpecialInstructions(models.Model):
    item_revision = models.ForeignKey(ItemRevision, models.DO_NOTHING, db_column='item_revision')
    note = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'item_special_instructions'


class ItemTransitionRules(models.Model):
    item_rev_in = models.ForeignKey(ItemRevision, models.DO_NOTHING, related_name="item_in_revision", db_column='item_rev_in')
    process = models.ForeignKey('Processes', models.DO_NOTHING)
    item_rev_out = models.ForeignKey(ItemRevision, models.DO_NOTHING, related_name="item_out_revision",  db_column='item_rev_out')

    class Meta:
        managed = False
        db_table = 'item_transition_rules'
        unique_together = (('item_rev_in', 'process', 'item_rev_out'),)


class Item(models.Model):
    item_number = models.CharField(unique=True, max_length=50)
    pref_vendor = models.ForeignKey('Vendors', models.DO_NOTHING, db_column='pref_vendor')
    def_uom = models.ForeignKey('Uom', models.DO_NOTHING, db_column='def_uom')
    live_inv = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.item_number

    class Meta:
        managed = False
        db_table = 'items'


class Kitparts(models.Model):
    kit = models.ForeignKey('Kits', models.DO_NOTHING)
    partqty = models.IntegerField(db_column='PartQty')  # Field name made lowercase.
    partuom = models.ForeignKey('Uom', models.DO_NOTHING, db_column='PartUOM')  # Field name made lowercase.
    item_rev = models.ForeignKey(ItemRevision, models.DO_NOTHING, related_name='kit_item_revision', db_column='item_rev')
    part_rev = models.ForeignKey(ItemRevision, models.DO_NOTHING, related_name='part_item_revision', db_column='part_rev')

    class Meta:
        managed = False
        db_table = 'kitparts'


class Kits(models.Model):
    kitname = models.CharField(db_column='KitName', max_length=50)  # Field name made lowercase.
    bagtype = models.IntegerField(db_column='BagType')  # Field name made lowercase.
    boxtype = models.SmallIntegerField(db_column='BoxType')  # Field name made lowercase.
    ctnqty = models.IntegerField(db_column='CtnQty')  # Field name made lowercase.
    item_revision = models.ForeignKey(ItemRevision, models.DO_NOTHING, db_column='item_revision')

    class Meta:
        managed = False
        db_table = 'kits'


class MatReqLines(models.Model):
    report = models.ForeignKey('MatReqs', models.DO_NOTHING)
    part_num = models.CharField(max_length=50)
    job = models.CharField(max_length=25)
    issued = models.IntegerField()
    job_qty = models.IntegerField()
    need_date = models.DateField()
    item_revision = models.ForeignKey(ItemRevision, models.DO_NOTHING, db_column='item_revision')

    class Meta:
        managed = False
        db_table = 'mat_req_lines'


class MatReqs(models.Model):
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mat_reqs'


class MonthNames(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'month_names'


class NCiSessions(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    ip_address = models.CharField(max_length=45)
    timestamp = models.IntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'n_ci_sessions'


class OldOrderlines(models.Model):
    ol_id = models.IntegerField()
    o = models.ForeignKey('Orders', models.DO_NOTHING, db_column='O_id')  # Field name made lowercase.
    partnum = models.CharField(db_column='partNum', max_length=50)  # Field name made lowercase.
    item_id = models.IntegerField()
    item_rev = models.IntegerField()
    quantity = models.IntegerField()
    duedate = models.DateField(db_column='dueDate')  # Field name made lowercase.
    shipdate = models.DateField(db_column='shipDate', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField()
    chg_date = models.DateTimeField()
    action = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'old_orderlines'


class OrderStatus(models.Model):
    status = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'order_status'


class OrderlineNotes(models.Model):
    ol = models.ForeignKey('Orderlines', models.DO_NOTHING, unique=True)
    note = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'orderline_notes'


class Orderlines(models.Model):
    o = models.ForeignKey('Orders', models.DO_NOTHING, db_column='O_id')  # Field name made lowercase.
    quantity = models.IntegerField()
    uom = models.ForeignKey('Uom', models.DO_NOTHING, db_column='uom')
    duedate = models.DateField(db_column='dueDate')  # Field name made lowercase.
    shipdate = models.DateField(db_column='shipDate', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField()
    item_rev = models.ForeignKey(ItemRevision, models.DO_NOTHING, db_column='item_rev', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderlines'


class Orders(models.Model):
    custid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='custId')  # Field name made lowercase.
    custpo = models.CharField(db_column='custPo', max_length=40)  # Field name made lowercase.
    o_date = models.DateField(db_column='O_date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'
        unique_together = (('custid', 'custpo'),)


class Part(models.Model):
    partnumber = models.CharField(db_column='PartNumber', max_length=50)  # Field name made lowercase.
    partdesc = models.CharField(db_column='PartDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orderqty = models.IntegerField(db_column='orderQty')  # Field name made lowercase.
    size = models.CharField(max_length=30)
    origin = models.CharField(max_length=20)
    clot = models.CharField(db_column='cLot', max_length=25, blank=True, null=True)  # Field name made lowercase.
    item_revision = models.ForeignKey(ItemRevision, models.DO_NOTHING, db_column='item_revision', unique=True)

    class Meta:
        managed = False
        db_table = 'parts'


class PjItems(models.Model):
    job_id = models.IntegerField()
    part_num = models.CharField(max_length=50)
    item_id = models.IntegerField()
    qty = models.IntegerField()
    lot = models.CharField(max_length=30)
    label_type = models.CharField(max_length=5)
    item_revision = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pj_items'


class Printjob(models.Model):
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'printjob'


class ProcessLabelJobs(models.Model):
    job_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'process_label_jobs'


class ProcessLabels(models.Model):
    plj = models.ForeignKey(ProcessLabelJobs, models.DO_NOTHING)
    item_revision = models.ForeignKey(ItemRevision, models.DO_NOTHING, db_column='item_revision')
    total_boxes = models.SmallIntegerField()
    box_number = models.SmallIntegerField()
    po_number = models.CharField(max_length=15)
    process = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'process_labels'


class Processes(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Companies, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'processes'


class ProductionQueue(models.Model):
    id = models.IntegerField(primary_key=True)
    order_line_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'production_queue'


class PurchaseOrderLines(models.Model):
    po = models.ForeignKey('PurchaseOrders', models.DO_NOTHING)
    qty = models.IntegerField()
    uom = models.ForeignKey('Uom', models.DO_NOTHING, db_column='uom')
    exp_date = models.DateField()
    complete = models.IntegerField()
    item_revision = models.ForeignKey(ItemRevision, models.DO_NOTHING, db_column='item_revision')
    ack_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'purchase_order_lines'


class PurchaseOrders(models.Model):
    po_number = models.CharField(unique=True, max_length=20)
    date = models.DateField()
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    terms = models.CharField(max_length=50)
    ship = models.CharField(max_length=50)
    old_po_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'purchase_orders'


class RevNotes(models.Model):
    item_revision = models.ForeignKey(ItemRevision, models.DO_NOTHING)
    note = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'rev_notes'


class RevisionLevels(models.Model):
    version_code = models.IntegerField()
    version_name = models.CharField(max_length=50)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'revision_levels'


class ShipmentParts(models.Model):
    shipment = models.ForeignKey('Shipments', models.DO_NOTHING, db_column='shipment')
    qty = models.IntegerField()
    uom = models.ForeignKey('Uom', models.DO_NOTHING, db_column='uom')
    billed = models.IntegerField()
    item_revision = models.ForeignKey(ItemRevision, models.DO_NOTHING, db_column='item_revision')

    class Meta:
        managed = False
        db_table = 'shipment_parts'


class Shipments(models.Model):
    company = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company')
    ship_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'shipments'


class Uom(models.Model):
    name = models.CharField(max_length=20)
    abbrv = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'uom'


class UomConversions(models.Model):
    item_revision = models.ForeignKey(ItemRevision, models.DO_NOTHING, db_column='item_revision', blank=True, null=True)
    uom_in = models.ForeignKey(Uom, models.DO_NOTHING, related_name='uom_in', db_column='uom_in')
    uom_out = models.ForeignKey(Uom, models.DO_NOTHING, related_name='uom_out', db_column='uom_out')
    rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'uom_conversions'
        unique_together = (('item_revision', 'uom_in', 'uom_out'),)


class UomParents(models.Model):
    uom = models.ForeignKey(Uom, models.DO_NOTHING, related_name='child_uom')
    parent_uom = models.ForeignKey(Uom, models.DO_NOTHING, related_name='parent_uom')

    class Meta:
        managed = False
        db_table = 'uom_parents'
        unique_together = (('uom', 'parent_uom'),)


class Users(models.Model):
    lastname = models.CharField(db_column='lastName', max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=30)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='companyId')  # Field name made lowercase.
    accesslevel = models.IntegerField(db_column='accessLevel')  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=24)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Vendors(models.Model):
    company = models.ForeignKey(Companies, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vendors'


class VmiInventory(models.Model):
    item_revision = models.IntegerField()
    qty = models.IntegerField()
    last_checked = models.DateField()
    location = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vmi_inventory'
        unique_together = (('item_revision', 'location'),)


class VmiLabels(models.Model):
    part = models.CharField(db_column='Part', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vmi_labels'


class VmiLocations(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vmi_locations'
