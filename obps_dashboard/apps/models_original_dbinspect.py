# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.db import models


class Bitstream(models.Model):
    bitstream_id = models.IntegerField(blank=True, null=True)
    bitstream_format = models.ForeignKey('Bitstreamformatregistry', models.DO_NOTHING, blank=True, null=True)
    size_bytes = models.BigIntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=64, blank=True, null=True)
    checksum_algorithm = models.CharField(max_length=32, blank=True, null=True)
    internal_id = models.CharField(max_length=256, blank=True, null=True)
    deleted = models.NullBooleanField()
    store_number = models.IntegerField(blank=True, null=True)
    sequence_id = models.IntegerField(blank=True, null=True)
    uuid = models.ForeignKey('Dspaceobject', models.DO_NOTHING, db_column='uuid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'bitstream'


class Bitstreamformatregistry(models.Model):
    bitstream_format_id = models.IntegerField(primary_key=True)
    mimetype = models.CharField(max_length=256, blank=True, null=True)
    short_description = models.CharField(unique=True, max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    support_level = models.IntegerField(blank=True, null=True)
    internal = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'bitstreamformatregistry'


class Bundle(models.Model):
    bundle_id = models.IntegerField(blank=True, null=True)
    uuid = models.ForeignKey('Dspaceobject', models.DO_NOTHING, db_column='uuid', primary_key=True)
    primary_bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bundle'


class Bundle2Bitstream(models.Model):
    bitstream_order_legacy = models.IntegerField(blank=True, null=True)
    bundle = models.ForeignKey(Bundle, models.DO_NOTHING)
    bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, primary_key=True)
    bitstream_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bundle2bitstream'
        unique_together = (('bitstream', 'bundle', 'bitstream_order'),)


class ChecksumHistory(models.Model):
    check_id = models.BigAutoField(primary_key=True)
    process_start_date = models.DateTimeField(blank=True, null=True)
    process_end_date = models.DateTimeField(blank=True, null=True)
    checksum_expected = models.CharField(max_length=-1, blank=True, null=True)
    checksum_calculated = models.CharField(max_length=100, blank=True, null=True)
    result = models.ForeignKey('ChecksumResults', models.DO_NOTHING, db_column='result', blank=True, null=True)
    bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checksum_history'


class ChecksumResults(models.Model):
    result_code = models.CharField(primary_key=True, max_length=-1)
    result_description = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checksum_results'


class Collection(models.Model):
    collection_id = models.IntegerField(blank=True, null=True)
    uuid = models.ForeignKey('Dspaceobject', models.DO_NOTHING, db_column='uuid', primary_key=True)
    workflow_step_1 = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='workflow_step_1', blank=True, null=True)
    workflow_step_2 = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='workflow_step_2', blank=True, null=True)
    workflow_step_3 = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='workflow_step_3', blank=True, null=True)
    submitter = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='submitter', blank=True, null=True)
    template_item_id = models.UUIDField(blank=True, null=True)
    logo_bitstream_id = models.UUIDField(blank=True, null=True)
    admin = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='admin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection'


class Collection2Item(models.Model):
    collection = models.ForeignKey(Collection, models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey('Item', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'collection2item'
        unique_together = (('collection', 'item'),)


class Community(models.Model):
    community_id = models.IntegerField(blank=True, null=True)
    uuid = models.ForeignKey('Dspaceobject', models.DO_NOTHING, db_column='uuid', primary_key=True)
    admin = models.ForeignKey('Epersongroup', models.DO_NOTHING, db_column='admin', blank=True, null=True)
    logo_bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community'


class Community2Collection(models.Model):
    collection = models.ForeignKey(Collection, models.DO_NOTHING, primary_key=True)
    community = models.ForeignKey(Community, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community2collection'
        unique_together = (('collection', 'community'),)


class Community2Community(models.Model):
    parent_comm = models.ForeignKey(Community, models.DO_NOTHING, primary_key=True)
    child_comm = models.ForeignKey(Community, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community2community'
        unique_together = (('parent_comm', 'child_comm'),)


class Doi(models.Model):
    doi_id = models.IntegerField(primary_key=True)
    doi = models.CharField(unique=True, max_length=256, blank=True, null=True)
    resource_type_id = models.IntegerField(blank=True, null=True)
    resource_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    dspace_object = models.ForeignKey('Dspaceobject', models.DO_NOTHING, db_column='dspace_object', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doi'


class Dspaceobject(models.Model):
    uuid = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dspaceobject'


class Eperson(models.Model):
    eperson_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=64, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    salt = models.CharField(max_length=32, blank=True, null=True)
    digest_algorithm = models.CharField(max_length=16, blank=True, null=True)
    can_log_in = models.NullBooleanField()
    require_certificate = models.NullBooleanField()
    self_registered = models.NullBooleanField()
    last_active = models.DateTimeField(blank=True, null=True)
    sub_frequency = models.IntegerField(blank=True, null=True)
    netid = models.CharField(max_length=64, blank=True, null=True)
    uuid = models.ForeignKey(Dspaceobject, models.DO_NOTHING, db_column='uuid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'eperson'


class Epersongroup(models.Model):
    eperson_group_id = models.IntegerField(blank=True, null=True)
    uuid = models.ForeignKey(Dspaceobject, models.DO_NOTHING, db_column='uuid', primary_key=True)
    permanent = models.NullBooleanField()
    name = models.CharField(unique=True, max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'epersongroup'


class Epersongroup2Eperson(models.Model):
    eperson_group = models.ForeignKey(Epersongroup, models.DO_NOTHING, primary_key=True)
    eperson = models.ForeignKey(Eperson, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'epersongroup2eperson'
        unique_together = (('eperson_group', 'eperson'),)


class Epersongroup2Workspaceitem(models.Model):
    workspace_item = models.ForeignKey('Workspaceitem', models.DO_NOTHING, primary_key=True)
    eperson_group = models.ForeignKey(Epersongroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'epersongroup2workspaceitem'
        unique_together = (('workspace_item', 'eperson_group'),)


class Fileextension(models.Model):
    file_extension_id = models.IntegerField(primary_key=True)
    bitstream_format = models.ForeignKey(Bitstreamformatregistry, models.DO_NOTHING, blank=True, null=True)
    extension = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fileextension'


class Group2Group(models.Model):
    parent = models.ForeignKey(Epersongroup, models.DO_NOTHING, primary_key=True)
    child = models.ForeignKey(Epersongroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group2group'
        unique_together = (('parent', 'child'),)


class Group2Groupcache(models.Model):
    parent = models.ForeignKey(Epersongroup, models.DO_NOTHING, primary_key=True)
    child = models.ForeignKey(Epersongroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group2groupcache'
        unique_together = (('parent', 'child'),)


class Handle(models.Model):
    handle_id = models.IntegerField(primary_key=True)
    handle = models.CharField(unique=True, max_length=256, blank=True, null=True)
    resource_type_id = models.IntegerField(blank=True, null=True)
    resource_legacy_id = models.IntegerField(blank=True, null=True)
    resource = models.ForeignKey(Dspaceobject, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'handle'


class HarvestedCollection(models.Model):
    harvest_type = models.IntegerField(blank=True, null=True)
    oai_source = models.CharField(max_length=-1, blank=True, null=True)
    oai_set_id = models.CharField(max_length=-1, blank=True, null=True)
    harvest_message = models.CharField(max_length=-1, blank=True, null=True)
    metadata_config_id = models.CharField(max_length=-1, blank=True, null=True)
    harvest_status = models.IntegerField(blank=True, null=True)
    harvest_start_time = models.DateTimeField(blank=True, null=True)
    last_harvested = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'harvested_collection'


class HarvestedItem(models.Model):
    last_harvested = models.DateTimeField(blank=True, null=True)
    oai_id = models.CharField(max_length=-1, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    item = models.ForeignKey('Item', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'harvested_item'


class Item(models.Model):
    item_id = models.IntegerField(blank=True, null=True)
    in_archive = models.NullBooleanField()
    withdrawn = models.NullBooleanField()
    discoverable = models.NullBooleanField()
    last_modified = models.DateTimeField(blank=True, null=True)
    uuid = models.ForeignKey(Dspaceobject, models.DO_NOTHING, db_column='uuid', primary_key=True)
    submitter = models.ForeignKey(Eperson, models.DO_NOTHING, blank=True, null=True)
    owning_collection = models.ForeignKey(Collection, models.DO_NOTHING, db_column='owning_collection', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class Item2Bundle(models.Model):
    bundle = models.ForeignKey(Bundle, models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'item2bundle'
        unique_together = (('bundle', 'item'),)


class Metadatafieldregistry(models.Model):
    metadata_field_id = models.AutoField(primary_key=True)
    metadata_schema = models.ForeignKey('Metadataschemaregistry', models.DO_NOTHING)
    element = models.CharField(max_length=64, blank=True, null=True)
    qualifier = models.CharField(max_length=64, blank=True, null=True)
    scope_note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadatafieldregistry'


class Metadataschemaregistry(models.Model):
    metadata_schema_id = models.AutoField(primary_key=True)
    namespace = models.CharField(unique=True, max_length=256, blank=True, null=True)
    short_id = models.CharField(unique=True, max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadataschemaregistry'


class Metadatavalue(models.Model):
    metadata_value_id = models.AutoField(primary_key=True)
    metadata_field = models.ForeignKey(Metadatafieldregistry, models.DO_NOTHING, blank=True, null=True)
    text_value = models.TextField(blank=True, null=True)
    text_lang = models.CharField(max_length=24, blank=True, null=True)
    place = models.IntegerField(blank=True, null=True)
    authority = models.CharField(max_length=100, blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    dspace_object = models.ForeignKey(Dspaceobject, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadatavalue'


class MostRecentChecksum(models.Model):
    to_be_processed = models.BooleanField()
    expected_checksum = models.CharField(max_length=-1)
    current_checksum = models.CharField(max_length=-1)
    last_process_start_date = models.DateTimeField()
    last_process_end_date = models.DateTimeField()
    checksum_algorithm = models.CharField(max_length=-1)
    matched_prev_checksum = models.BooleanField()
    result = models.ForeignKey(ChecksumResults, models.DO_NOTHING, db_column='result', blank=True, null=True)
    bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'most_recent_checksum'


class Registrationdata(models.Model):
    registrationdata_id = models.IntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=64, blank=True, null=True)
    token = models.CharField(max_length=48, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registrationdata'


class Requestitem(models.Model):
    requestitem_id = models.IntegerField(primary_key=True)
    token = models.CharField(unique=True, max_length=48, blank=True, null=True)
    allfiles = models.NullBooleanField()
    request_email = models.CharField(max_length=64, blank=True, null=True)
    request_name = models.CharField(max_length=64, blank=True, null=True)
    request_date = models.DateTimeField(blank=True, null=True)
    accept_request = models.NullBooleanField()
    decision_date = models.DateTimeField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    request_message = models.TextField(blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    bitstream = models.ForeignKey(Bitstream, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requestitem'


class Resourcepolicy(models.Model):
    policy_id = models.IntegerField(primary_key=True)
    resource_type_id = models.IntegerField(blank=True, null=True)
    resource_id = models.IntegerField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    rpname = models.CharField(max_length=30, blank=True, null=True)
    rptype = models.CharField(max_length=30, blank=True, null=True)
    rpdescription = models.TextField(blank=True, null=True)
    eperson = models.ForeignKey(Eperson, models.DO_NOTHING, blank=True, null=True)
    epersongroup = models.ForeignKey(Epersongroup, models.DO_NOTHING, blank=True, null=True)
    dspace_object = models.ForeignKey(Dspaceobject, models.DO_NOTHING, db_column='dspace_object', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resourcepolicy'


class SchemaVersion(models.Model):
    installed_rank = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'schema_version'


class Site(models.Model):
    uuid = models.ForeignKey(Dspaceobject, models.DO_NOTHING, db_column='uuid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'site'


class Subscription(models.Model):
    subscription_id = models.IntegerField(primary_key=True)
    eperson = models.ForeignKey(Eperson, models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription'


class Tasklistitem(models.Model):
    tasklist_id = models.IntegerField(primary_key=True)
    workflow = models.ForeignKey('Workflowitem', models.DO_NOTHING, blank=True, null=True)
    eperson = models.ForeignKey(Eperson, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasklistitem'


class Versionhistory(models.Model):
    versionhistory_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'versionhistory'


class Versionitem(models.Model):
    versionitem_id = models.IntegerField(primary_key=True)
    version_number = models.IntegerField(blank=True, null=True)
    version_date = models.DateTimeField(blank=True, null=True)
    version_summary = models.CharField(max_length=255, blank=True, null=True)
    versionhistory = models.ForeignKey(Versionhistory, models.DO_NOTHING, blank=True, null=True)
    eperson = models.ForeignKey(Eperson, models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'versionitem'


class Webapp(models.Model):
    webapp_id = models.IntegerField(primary_key=True)
    appname = models.CharField(max_length=32, blank=True, null=True)
    url = models.CharField(max_length=-1, blank=True, null=True)
    started = models.DateTimeField(blank=True, null=True)
    isui = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webapp'


class Workflowitem(models.Model):
    workflow_id = models.IntegerField(primary_key=True)
    state = models.IntegerField(blank=True, null=True)
    multiple_titles = models.NullBooleanField()
    published_before = models.NullBooleanField()
    multiple_files = models.NullBooleanField()
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(Eperson, models.DO_NOTHING, db_column='owner', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflowitem'


class Workspaceitem(models.Model):
    workspace_item_id = models.IntegerField(primary_key=True)
    multiple_titles = models.NullBooleanField()
    published_before = models.NullBooleanField()
    multiple_files = models.NullBooleanField()
    stage_reached = models.IntegerField(blank=True, null=True)
    page_reached = models.IntegerField(blank=True, null=True)
    item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workspaceitem'
