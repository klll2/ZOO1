from django.db import models


class Animal(models.Model):
    anm_id = models.IntegerField(primary_key=True)
    anm_name = models.CharField(max_length=45)
    anm_spcs = models.CharField(max_length=45)
    anm_city = models.CharField(max_length=45)
    anm_sex = models.CharField(max_length=20)
    anm_birth = models.DateField(blank=True, null=True)
    anm_rct = models.CharField(max_length=45)
    anm_img = models.TextField(blank=True, null=True)
    anm_food = models.CharField(max_length=45, blank=True, null=True)
    zone = models.ForeignKey('Zone', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'animal'


class Area(models.Model):
    area_id = models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=20)
    area_loc = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'area'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    question = models.ForeignKey('BlogQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_answer'


class BlogQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blog_question'


class CheckLog(models.Model):
    anm = models.OneToOneField(Animal, models.DO_NOTHING, primary_key=True)
    clog_tm = models.TimeField()
    clog_food = models.CharField(max_length=45)
    clog_bf = models.IntegerField()
    clog_lch = models.IntegerField()
    clog_dn = models.IntegerField()
    clog_mc = models.CharField(max_length=45, blank=True, null=True)
    clog_mm = models.IntegerField(blank=True, null=True)
    clog_lm = models.IntegerField(blank=True, null=True)
    clog_em = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'check_log'


class DetailLog(models.Model):
    dlog_id = models.IntegerField(primary_key=True)
    dlog_cgr = models.CharField(max_length=20)
    dlog_con = models.CharField(max_length=100)
    dlog_dt = models.DateTimeField()
    anm = models.ForeignKey(Animal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'detail_log'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Parttime(models.Model):
    pt_id = models.IntegerField(primary_key=True)
    pt_name = models.IntegerField()
    pt_start = models.TimeField()
    pt_end = models.TimeField()

    class Meta:
        managed = False
        db_table = 'parttime'


class Zone(models.Model):
    zone_id = models.IntegerField(primary_key=True)
    zone_name = models.CharField(max_length=20)
    zone_max = models.IntegerField()
    zone_loc = models.CharField(max_length=45)
    area = models.ForeignKey(Area, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'zone'


class Zookeeper(models.Model):
    zkp_id = models.IntegerField(primary_key=True)
    zkp_name = models.CharField(max_length=11)
    zkp_call = models.CharField(max_length=11)
    zkp_carr = models.CharField(max_length=10)
    zone = models.ForeignKey(Zone, models.DO_NOTHING)
    pt = models.ForeignKey(Parttime, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'zookeeper'