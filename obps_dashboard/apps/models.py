# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Ganalytics_obpsystem(models.Model):
    id = models.AutoField(primary_key=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    users_num_total = models.BigIntegerField(blank=True, null=True)
    users_num_new = models.BigIntegerField(blank=True, null=True)
    visits_num = models.BigIntegerField(blank=True, null=True)
    countries_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"ganalytics_obpsystem'

class Ganalytics_obpsystem_countries(models.Model):
    id = models.AutoField(primary_key=True)
    users = models.BigIntegerField(blank=True, null=True)
    sessions = models.BigIntegerField(blank=True, null=True)
    country = models.CharField(max_length=40,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"ganalytics_obpsystem_countries'

class Ganalytics_obpsorg(models.Model):
    id = models.AutoField(primary_key=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    users_num_total = models.BigIntegerField(blank=True, null=True)
    users_num_new = models.BigIntegerField(blank=True, null=True)
    visits_num = models.BigIntegerField(blank=True, null=True)
    countries_num = models.BigIntegerField(blank=True, null=True)
    docs_access_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"ganalytics_obpsorg'

class Ganalytics_obpsorg_countries(models.Model):
    id = models.AutoField(primary_key=True)
    users = models.BigIntegerField(blank=True, null=True)
    sessions = models.BigIntegerField(blank=True, null=True)
    country = models.CharField(max_length=40,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"ganalytics_obpsorg_countries'

class Ganalytics_obpsorg_docs(models.Model):
    id = models.AutoField(primary_key=True)
    doc_path = models.TextField(blank=True, null=True)
    countries = models.BigIntegerField(blank=True, null=True)
    users = models.BigIntegerField(blank=True, null=True)
    sessions = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"ganalytics_obpsorg_docs'


class Ganalytics_obpsorg_lastmonth(models.Model):
    id = models.AutoField(primary_key=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    users_num_total = models.BigIntegerField(blank=True, null=True)
    users_num_new = models.BigIntegerField(blank=True, null=True)
    visits_num = models.BigIntegerField(blank=True, null=True)
    countries_num = models.BigIntegerField(blank=True, null=True)
    docs_access_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"ganalytics_obpsorg_lastmonth'

class Ganalytics_obpsorg_lastmonth_countries(models.Model):
    id = models.AutoField(primary_key=True)
    users = models.BigIntegerField(blank=True, null=True)
    sessions = models.BigIntegerField(blank=True, null=True)
    country = models.CharField(max_length=40,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"ganalytics_obpsorg_lastmonth_countries'

class Ganalytics_obpsorg_lastmonth_docs(models.Model):
    id = models.AutoField(primary_key=True)
    doc_path = models.TextField(blank=True, null=True)
    countries = models.BigIntegerField(blank=True, null=True)
    users = models.BigIntegerField(blank=True, null=True)
    sessions = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"ganalytics_obpsorg_lastmonth_docs'


class Conferences(models.Model):
    id = models.AutoField(primary_key=True)
    activity_code = models.TextField(blank=True, null=True)
    activity_name = models.TextField(blank=True, null=True)
    event = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"conferences'


class Newsletter(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    list_name = models.TextField(blank=True, null=True)
    subject_line = models.TextField(blank=True, null=True)
    emails_sent = models.BigIntegerField(blank=True, null=True)
    unsubscribed = models.BigIntegerField(blank=True, null=True)
    hard_bounces = models.BigIntegerField(blank=True, null=True)
    soft_bounces = models.BigIntegerField(blank=True, null=True)
    opens_total = models.BigIntegerField(blank=True, null=True)
    unique_opens = models.BigIntegerField(blank=True, null=True)
    clicks_total = models.BigIntegerField(blank=True, null=True)
    unique_clicks = models.BigIntegerField(blank=True, null=True)
    unique_subscriber_clicks = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"newsletter'

class Newsletter_subscribers_grouth(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    subscribed = models.IntegerField(blank=True, null=True)
    list_change_mom = models.IntegerField(blank=True, null=True)
    list_change_yoy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"newsletter_subscribers_grouth'

class Newsletter_locations(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.TextField(blank=True, null=True)
    cc = models.TextField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"newsletter_locations'

class Dspace_records(models.Model):
    id = models.AutoField(primary_key=True)
    dspace_object_id = models.TextField(blank=True, null=True)
    handle = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    maturity_level = models.TextField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    doi = models.TextField(blank=True, null=True)
    doi_obp = models.TextField(blank=True, null=True)
    submitter_id = models.TextField(blank=True, null=True)
    publisher_place = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    year_created = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"dspace_records'

class Dspace_record_disciplines(models.Model):
    id = models.AutoField(primary_key=True)
    dspace_object_id = models.TextField(blank=True, null=True)
    discipline_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"dspace_record_disciplines'

class Dspace_record_bptypes(models.Model):
    id = models.AutoField(primary_key=True)
    dspace_object_id = models.TextField(blank=True, null=True)
    bp_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"dspace_record_bptypes'

class Dspace_record_adoptiontypes(models.Model):
    id = models.AutoField(primary_key=True)
    dspace_object_id = models.TextField(blank=True, null=True)
    adoption_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"dspace_record_adoptiontypes'

class Dspace_collections(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"dspace_collections'

class Dspace_communities(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"dspace_communities'

class Dspace_record_eovs(models.Model):
    id = models.AutoField(primary_key=True)
    dspace_object_id = models.TextField(blank=True, null=True)
    eov = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"dspace_record_eovs'

class Dspace_record_sdgs(models.Model):
    id = models.AutoField(primary_key=True)
    dspace_object_id = models.TextField(blank=True, null=True)
    sdg = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metrics\".\"dspace_record_sdgs'

class Communities_engagement(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    user_community = models.TextField(blank=True, null=True)
    contacts = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    lead = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'metrics\".\"communities_engagement'

class Obps_workshops(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    country_celebration = models.TextField(blank=True, null=True)
    num_participants = models.IntegerField(blank=True, null=True)
    num_participants_countries_origin = models.IntegerField(blank=True, null=True)
    num_support_organizations = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'metrics\".\"obps_workshops'

# ### DSPACE DATABASE MODELS  ###
# class Bitstream(models.Model):
#     bitstream_id = models.IntegerField(blank=True, null=True)
#     bitstream_format = models.ForeignKey('Bitstreamformatregistry', models.DO_NOTHING, blank=True, null=True)
#     size_bytes = models.BigIntegerField(blank=True, null=True)
#     checksum = models.CharField(max_length=64, blank=True, null=True)
#     checksum_algorithm = models.CharField(max_length=32, blank=True, null=True)
#     internal_id = models.CharField(max_length=256, blank=True, null=True)
#     deleted = models.NullBooleanField()
#     store_number = models.IntegerField(blank=True, null=True)
#     sequence_id = models.IntegerField(blank=True, null=True)
#     uuid = models.ForeignKey('Dspaceobject', models.DO_NOTHING, db_column='uuid', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitstream'
#
#
# class Bitstreamformatregistry(models.Model):
#     bitstream_format_id = models.IntegerField(primary_key=True)
#     mimetype = models.CharField(max_length=256, blank=True, null=True)
#     short_description = models.CharField(unique=True, max_length=128, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     support_level = models.IntegerField(blank=True, null=True)
#     internal = models.NullBooleanField()
#
#     class Meta:
#         managed = False
#         db_table = 'bitstreamformatregistry'
#
#
# class Bundle(models.Model):
#     bundle_id = models.IntegerField(blank=True, null=True)
#     uuid = models.ForeignKey('Dspaceobject', models.DO_NOTHING, db_column='uuid', primary_key=True)
#     primary_bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bundle'
#
#
# class Bundle2Bitstream(models.Model):
#     bitstream_order_legacy = models.IntegerField(blank=True, null=True)
#     bundle = models.ForeignKey(Bundle, models.DO_NOTHING)
#     bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, primary_key=True)
#     bitstream_order = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'bundle2bitstream'
#         unique_together = (('bitstream', 'bundle', 'bitstream_order'),)
#
#
# class ChecksumHistory(models.Model):
#     check_id = models.BigAutoField(primary_key=True)
#     process_start_date = models.DateTimeField(blank=True, null=True)
#     process_end_date = models.DateTimeField(blank=True, null=True)
#     checksum_expected = models.CharField(max_length=100, blank=True, null=True)
#     checksum_calculated = models.CharField(max_length=100, blank=True, null=True)
#     result = models.ForeignKey('ChecksumResults', models.DO_NOTHING, db_column='result', blank=True, null=True)
#     bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'checksum_history'
#
#
# class ChecksumResults(models.Model):
#     result_code = models.CharField(primary_key=True, max_length=100)
#     result_description = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'checksum_results'
#
#
# class Collection(models.Model):
#     collection_id = models.IntegerField(blank=True, null=True)
#     uuid = models.ForeignKey('Dspaceobject', models.DO_NOTHING, db_column='uuid', primary_key=True)
#     workflow_step_1 = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='workflow_step_1', blank=True, null=True, related_name='workflow_step_1')
#     workflow_step_2 = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='workflow_step_2', blank=True, null=True, related_name='workflow_step_2')
#     workflow_step_3 = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='workflow_step_3', blank=True, null=True, related_name='workflow_step_3')
#     submitter = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='submitter', blank=True, null=True)
#     template_item_id = models.UUIDField(blank=True, null=True)
#     logo_bitstream_id = models.UUIDField(blank=True, null=True)
#     admin = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='admin', blank=True, null=True, related_name='admin')
#
#     class Meta:
#         managed = False
#         db_table = 'collection'
#
#
# class Collection2Item(models.Model):
#     collection = models.ForeignKey(Collection, models.DO_NOTHING, primary_key=True)
#     item = models.ForeignKey('Item', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'collection2item'
#         unique_together = (('collection', 'item'),)
#
#
# class Community(models.Model):
#     community_id = models.IntegerField(blank=True, null=True)
#     uuid = models.ForeignKey('Dspaceobject', models.DO_NOTHING, db_column='uuid', primary_key=True)
#     admin = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='admin', blank=True, null=True)
#     logo_bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'community'
#
#
# class Community2Collection(models.Model):
#     collection = models.ForeignKey(Collection, models.DO_NOTHING, primary_key=True)
#     community = models.ForeignKey(Community, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'community2collection'
#         unique_together = (('collection', 'community'),)
#
#
# class Community2Community(models.Model):
#     parent_comm = models.ForeignKey(Community, models.DO_NOTHING, primary_key=True, related_name='parent_comm')
#     child_comm = models.ForeignKey(Community, models.DO_NOTHING, related_name='child_comm')
#
#     class Meta:
#         managed = False
#         db_table = 'community2community'
#         unique_together = (('parent_comm', 'child_comm'),)
#
#
# class Doi(models.Model):
#     doi_id = models.IntegerField(primary_key=True)
#     doi = models.CharField(unique=True, max_length=256, blank=True, null=True)
#     resource_type_id = models.IntegerField(blank=True, null=True)
#     resource_id = models.IntegerField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     dspace_object = models.ForeignKey('Dspaceobject', models.DO_NOTHING, db_column='dspace_object', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'doi'
#
#
# class Dspaceobject(models.Model):
#     uuid = models.UUIDField(primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'dspaceobject'
#
#
# class Eperson(models.Model):
#     eperson_id = models.IntegerField(blank=True, null=True)
#     email = models.CharField(unique=True, max_length=64, blank=True, null=True)
#     password = models.CharField(max_length=128, blank=True, null=True)
#     salt = models.CharField(max_length=32, blank=True, null=True)
#     digest_algorithm = models.CharField(max_length=16, blank=True, null=True)
#     can_log_in = models.NullBooleanField()
#     require_certificate = models.NullBooleanField()
#     self_registered = models.NullBooleanField()
#     last_active = models.DateTimeField(blank=True, null=True)
#     sub_frequency = models.IntegerField(blank=True, null=True)
#     netid = models.CharField(max_length=64, blank=True, null=True)
#     uuid = models.ForeignKey(Dspaceobject, models.DO_NOTHING, db_column='uuid', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'eperson'
#
#
# class Epersongroup(models.Model):
#     eperson_group_id = models.IntegerField(blank=True, null=True)
#     uuid = models.ForeignKey(Dspaceobject, models.DO_NOTHING, db_column='uuid', primary_key=True)
#     permanent = models.NullBooleanField()
#     name = models.CharField(unique=True, max_length=250, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'epersongroup'
#
#
# class Epersongroup2Eperson(models.Model):
#     eperson_group = models.ForeignKey(Epersongroup, models.DO_NOTHING, primary_key=True)
#     eperson = models.ForeignKey(Eperson, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'epersongroup2eperson'
#         unique_together = (('eperson_group', 'eperson'),)
#
#
# class Epersongroup2Workspaceitem(models.Model):
#     workspace_item = models.ForeignKey('Workspaceitem', models.DO_NOTHING, primary_key=True)
#     eperson_group = models.ForeignKey(Epersongroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'epersongroup2workspaceitem'
#         unique_together = (('workspace_item', 'eperson_group'),)
#
#
# class Fileextension(models.Model):
#     file_extension_id = models.IntegerField(primary_key=True)
#     bitstream_format = models.ForeignKey(Bitstreamformatregistry, models.DO_NOTHING, blank=True, null=True)
#     extension = models.CharField(max_length=16, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'fileextension'
#
#
# class Group2Group(models.Model):
#     parent = models.ForeignKey(Epersongroup, models.DO_NOTHING, primary_key=True, related_name='g2g_parent')
#     child = models.ForeignKey(Epersongroup, models.DO_NOTHING, related_name='g2g_child')
#
#     class Meta:
#         managed = False
#         db_table = 'group2group'
#         unique_together = (('parent', 'child'),)
#
#
# class Group2Groupcache(models.Model):
#     parent = models.ForeignKey(Epersongroup, models.DO_NOTHING, primary_key=True, related_name='g2gc_parent')
#     child = models.ForeignKey(Epersongroup, models.DO_NOTHING, related_name='g2gc_child')
#
#     class Meta:
#         managed = False
#         db_table = 'group2groupcache'
#         unique_together = (('parent', 'child'),)
#
#
# class Handle(models.Model):
#     handle_id = models.IntegerField(primary_key=True)
#     handle = models.CharField(unique=True, max_length=256, blank=True, null=True)
#     resource_type_id = models.IntegerField(blank=True, null=True)
#     resource_legacy_id = models.IntegerField(blank=True, null=True)
#     resource = models.ForeignKey(Dspaceobject, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'handle'
#
#
# class HarvestedCollection(models.Model):
#     harvest_type = models.IntegerField(blank=True, null=True)
#     oai_source = models.CharField(max_length=100, blank=True, null=True)
#     oai_set_id = models.CharField(max_length=100, blank=True, null=True)
#     harvest_message = models.CharField(max_length=100, blank=True, null=True)
#     metadata_config_id = models.CharField(max_length=100, blank=True, null=True)
#     harvest_status = models.IntegerField(blank=True, null=True)
#     harvest_start_time = models.DateTimeField(blank=True, null=True)
#     last_harvested = models.DateTimeField(blank=True, null=True)
#     id = models.IntegerField(primary_key=True)
#     collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'harvested_collection'
#
#
# class HarvestedItem(models.Model):
#     last_harvested = models.DateTimeField(blank=True, null=True)
#     oai_id = models.CharField(max_length=100, blank=True, null=True)
#     id = models.IntegerField(primary_key=True)
#     item = models.ForeignKey('Item', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'harvested_item'
#
#
# class Item(models.Model):
#     item_id = models.IntegerField(blank=True, null=True)
#     in_archive = models.NullBooleanField()
#     withdrawn = models.NullBooleanField()
#     discoverable = models.NullBooleanField()
#     last_modified = models.DateTimeField(blank=True, null=True)
#     uuid = models.ForeignKey(Dspaceobject, models.DO_NOTHING, db_column='uuid', primary_key=True)
#     submitter = models.ForeignKey(Eperson, models.DO_NOTHING, blank=True, null=True)
#     owning_collection = models.ForeignKey(Collection, models.DO_NOTHING, db_column='owning_collection', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'item'
#
#
# class Item2Bundle(models.Model):
#     bundle = models.ForeignKey(Bundle, models.DO_NOTHING, primary_key=True)
#     item = models.ForeignKey(Item, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'item2bundle'
#         unique_together = (('bundle', 'item'),)
#
#
# class Metadatafieldregistry(models.Model):
#     metadata_field_id = models.AutoField(primary_key=True)
#     metadata_schema = models.ForeignKey('Metadataschemaregistry', models.DO_NOTHING)
#     element = models.CharField(max_length=64, blank=True, null=True)
#     qualifier = models.CharField(max_length=64, blank=True, null=True)
#     scope_note = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'metadatafieldregistry'
#
#
# class Metadataschemaregistry(models.Model):
#     metadata_schema_id = models.AutoField(primary_key=True)
#     namespace = models.CharField(unique=True, max_length=256, blank=True, null=True)
#     short_id = models.CharField(unique=True, max_length=32, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'metadataschemaregistry'
#
#
# class Metadatavalue(models.Model):
#     metadata_value_id = models.AutoField(primary_key=True)
#     metadata_field = models.ForeignKey(Metadatafieldregistry, models.DO_NOTHING, blank=True, null=True)
#     text_value = models.TextField(blank=True, null=True)
#     text_lang = models.CharField(max_length=24, blank=True, null=True)
#     place = models.IntegerField(blank=True, null=True)
#     authority = models.CharField(max_length=100, blank=True, null=True)
#     confidence = models.IntegerField(blank=True, null=True)
#     dspace_object = models.ForeignKey(Dspaceobject, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'metadatavalue'
#
#
# class MostRecentChecksum(models.Model):
#     to_be_processed = models.BooleanField()
#     expected_checksum = models.CharField(max_length=100)
#     current_checksum = models.CharField(max_length=100)
#     last_process_start_date = models.DateTimeField()
#     last_process_end_date = models.DateTimeField()
#     checksum_algorithm = models.CharField(max_length=100)
#     matched_prev_checksum = models.BooleanField()
#     result = models.ForeignKey(ChecksumResults, models.DO_NOTHING, db_column='result', blank=True, null=True)
#     bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'most_recent_checksum'
#
#
# class Registrationdata(models.Model):
#     registrationdata_id = models.IntegerField(primary_key=True)
#     email = models.CharField(unique=True, max_length=64, blank=True, null=True)
#     token = models.CharField(max_length=48, blank=True, null=True)
#     expires = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'registrationdata'
#
#
# class Requestitem(models.Model):
#     requestitem_id = models.IntegerField(primary_key=True)
#     token = models.CharField(unique=True, max_length=48, blank=True, null=True)
#     allfiles = models.NullBooleanField()
#     request_email = models.CharField(max_length=64, blank=True, null=True)
#     request_name = models.CharField(max_length=64, blank=True, null=True)
#     request_date = models.DateTimeField(blank=True, null=True)
#     accept_request = models.NullBooleanField()
#     decision_date = models.DateTimeField(blank=True, null=True)
#     expires = models.DateTimeField(blank=True, null=True)
#     request_message = models.TextField(blank=True, null=True)
#     item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
#     bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'requestitem'
#
#
# class Resourcepolicy(models.Model):
#     policy_id = models.IntegerField(primary_key=True)
#     resource_type_id = models.IntegerField(blank=True, null=True)
#     resource_id = models.IntegerField(blank=True, null=True)
#     action_id = models.IntegerField(blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)
#     rpname = models.CharField(max_length=30, blank=True, null=True)
#     rptype = models.CharField(max_length=30, blank=True, null=True)
#     rpdescription = models.TextField(blank=True, null=True)
#     eperson = models.ForeignKey(Eperson, models.DO_NOTHING, blank=True, null=True)
#     epersongroup = models.ForeignKey(Epersongroup, models.DO_NOTHING, blank=True, null=True)
#     dspace_object = models.ForeignKey(Dspaceobject, models.DO_NOTHING, db_column='dspace_object', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'resourcepolicy'
#
#
# class SchemaVersion(models.Model):
#     installed_rank = models.IntegerField(primary_key=True)
#     version = models.CharField(max_length=50, blank=True, null=True)
#     description = models.CharField(max_length=200)
#     type = models.CharField(max_length=20)
#     script = models.CharField(max_length=1000)
#     checksum = models.IntegerField(blank=True, null=True)
#     installed_by = models.CharField(max_length=100)
#     installed_on = models.DateTimeField()
#     execution_time = models.IntegerField()
#     success = models.BooleanField()
#
#     class Meta:
#         managed = False
#         db_table = 'schema_version'
#
#
# class Site(models.Model):
#     uuid = models.ForeignKey(Dspaceobject, models.DO_NOTHING, db_column='uuid', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'site'
#
#
# class Subscription(models.Model):
#     subscription_id = models.IntegerField(primary_key=True)
#     eperson = models.ForeignKey(Eperson, models.DO_NOTHING, blank=True, null=True)
#     collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'subscription'
#
#
# class Tasklistitem(models.Model):
#     tasklist_id = models.IntegerField(primary_key=True)
#     workflow = models.ForeignKey('Workflowitem', models.DO_NOTHING, blank=True, null=True)
#     eperson = models.ForeignKey(Eperson, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tasklistitem'
#
#
# class Versionhistory(models.Model):
#     versionhistory_id = models.IntegerField(primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'versionhistory'
#
#
# class Versionitem(models.Model):
#     versionitem_id = models.IntegerField(primary_key=True)
#     version_number = models.IntegerField(blank=True, null=True)
#     version_date = models.DateTimeField(blank=True, null=True)
#     version_summary = models.CharField(max_length=255, blank=True, null=True)
#     versionhistory = models.ForeignKey(Versionhistory, models.DO_NOTHING, blank=True, null=True)
#     eperson = models.ForeignKey(Eperson, models.DO_NOTHING, blank=True, null=True)
#     item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'versionitem'
#
#
# class Webapp(models.Model):
#     webapp_id = models.IntegerField(primary_key=True)
#     appname = models.CharField(max_length=32, blank=True, null=True)
#     url = models.CharField(max_length=100, blank=True, null=True)
#     started = models.DateTimeField(blank=True, null=True)
#     isui = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'webapp'
#
#
# class Workflowitem(models.Model):
#     workflow_id = models.IntegerField(primary_key=True)
#     state = models.IntegerField(blank=True, null=True)
#     multiple_titles = models.NullBooleanField()
#     published_before = models.NullBooleanField()
#     multiple_files = models.NullBooleanField()
#     item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
#     collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)
#     owner = models.ForeignKey(Eperson, models.DO_NOTHING, db_column='owner', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'workflowitem'
#
#
# class Workspaceitem(models.Model):
#     workspace_item_id = models.IntegerField(primary_key=True)
#     multiple_titles = models.NullBooleanField()
#     published_before = models.NullBooleanField()
#     multiple_files = models.NullBooleanField()
#     stage_reached = models.IntegerField(blank=True, null=True)
#     page_reached = models.IntegerField(blank=True, null=True)
#     item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
#     collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'workspaceitem'
