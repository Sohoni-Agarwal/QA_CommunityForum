#This md5=staticmethod auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class AdminMasterTable(models.Model):
    admin_id = models.IntegerField(db_column='Admin_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    e_mail = models.TextField(db_column='E-mail', blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    is_super_admin = models.BooleanField(
        db_column='Is_Super Admin')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ADMIN_MASTER TABLE'


class AdminUserTable(models.Model):
    admin = models.ForeignKey(AdminMasterTable, models.DO_NOTHING, db_column='Admin_ID', blank=True,
                              null=True)  # Field name made lowercase.
    user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, db_column='User_ID', blank=True,
                             null=True)  # Field name made lowercase.
    sau = models.ForeignKey('SuperAdminAdminUserTable', models.DO_NOTHING, db_column='SAU_ID', blank=True,
                            null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADMIN_USER TABLE'


class IdentityMasterTable(models.Model):
    identity_id = models.IntegerField(db_column='Identity_ID', primary_key=True)  # Field name made lowercase.
    identity_type = models.CharField(db_column='Identity_Type', max_length=150, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IDENTITY_MASTER TABLE'


class NotificationsMasterTable(models.Model):
    notification_id = models.IntegerField(db_column='Notification_ID', primary_key=True)  # Field name made lowercase.
    notification_type = models.CharField(db_column='Notification_Type', max_length=150, blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTIFICATIONS_MASTER TABLE'


class PostsMasterTable(models.Model):
    post_id = models.IntegerField(db_column='Post_ID', primary_key=True)  # Field name made lowercase.
    post_type = models.CharField(db_column='Post_Type', max_length=150, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POSTS_MASTER TABLE'


class SuperAdminAdminUserTable(models.Model):
    super_admin_id = models.IntegerField(
        db_column='Super Admin_ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    admin = models.ForeignKey(AdminMasterTable, models.DO_NOTHING, db_column='Admin_ID')  # Field name made lowercase.
    user_id_from = models.ForeignKey('UserMasterTable', models.DO_NOTHING,
                                     db_column='User_ID From',
                                     related_name='user_id_from')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_id_to = models.ForeignKey('UserMasterTable', models.DO_NOTHING, db_column='User_ID To', blank=True,
                                   null=True,
                                   related_name='user_id_to')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sau_id = models.IntegerField(db_column='SAU_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SUPER ADMIN_ADMIN_USER TABLE'


class TopicsMasterTable(models.Model):
    topic_id = models.IntegerField(db_column='Topic_ID', primary_key=True)  # Field name made lowercase.
    topic_type = models.CharField(db_column='Topic_Type', max_length=150, blank=True,
                                  null=True)  # Field name made lowercase.
    topic_name = models.CharField(db_column='Topic_Name', max_length=150, blank=True,
                                  null=True)  # Field name made lowercase.
    topic_created_on = models.DateTimeField(db_column='Topic_Created_On', blank=True,
                                            null=True)  # Field name made lowercase.
    topic_description = models.TextField(db_column='Topic_Description', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOPICS_MASTER TABLE'


class UserAnswerTable(models.Model):
    answer_s_user = models.ForeignKey('UserMasterTable', models.DO_NOTHING, db_column="Answer's_User_ID", blank=True,
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    answer_id = models.IntegerField(db_column='Answer_ID', primary_key=True)  # Field name made lowercase.
    answer = models.CharField(db_column='Answer', max_length=150, blank=True, null=True)  # Field name made lowercase.
    question_id = models.IntegerField(db_column='Question_ID')  # Field name made lowercase.
    vote = models.ForeignKey('VoteMasterTable', models.DO_NOTHING, db_column='Vote_ID', blank=True,
                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_ANSWER TABLE'


class UserMasterTable(models.Model):
    objects = None
    user_id = models.IntegerField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=150, blank=True,
                                null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-mail', max_length=150, blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    date_joined = models.DateTimeField(db_column='Date_Joined', blank=True, null=True)  # Field name made lowercase.
    accounts_added = models.CharField(db_column='Accounts_Added', max_length=150, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_MASTER TABLE'

    @receiver(post_save, sender=User)
    def create_user_details(self, instance, created, **kwargs):
        if created:
            UserMasterTable.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def login_user_details(self, instance, **kwargs):
        instance.UserMasterTable.login()

    @receiver(post_save, sender=User)
    def save_user_details(self, instance, **kwargs):
        instance.UserMasterTable.save()


class UserNotificationTable(models.Model):
    user = models.ForeignKey(UserMasterTable, models.DO_NOTHING, db_column='User_ID', blank=True,
                             null=True)  # Field name made lowercase.
    notification = models.ForeignKey(NotificationsMasterTable, models.DO_NOTHING, db_column='Notification_ID',
                                     blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_NOTIFICATION TABLE'


class UserPostsIdentityTable(models.Model):
    user = models.ForeignKey(UserMasterTable, models.DO_NOTHING, db_column='User_ID', blank=True,
                             null=True)  # Field name made lowercase.
    post = models.ForeignKey(PostsMasterTable, models.DO_NOTHING, db_column='Post_ID', blank=True,
                             null=True)  # Field name made lowercase.
    identity = models.ForeignKey(IdentityMasterTable, models.DO_NOTHING, db_column='Identity_ID', blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_POSTS_IDENTITY TABLE'


class UserProfileTable(models.Model):
    user_profile_id = models.IntegerField(db_column='User_Profile_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(UserMasterTable, models.DO_NOTHING, db_column='User_ID', blank=True,
                             null=True)  # Field name made lowercase.
    profile_last_updated = models.DateTimeField(db_column='Profile_Last_Updated', blank=True,
                                                null=True)  # Field name made lowercase.
    employment_position = models.TextField(db_column='Employment_Position', blank=True,
                                           null=True)  # Field name made lowercase.
    company = models.TextField(db_column='Company', blank=True, null=True)  # Field name made lowercase.
    start_year = models.IntegerField(db_column='Start_Year', blank=True, null=True)  # Field name made lowercase.
    end_year = models.IntegerField(db_column='End_Year', blank=True, null=True)  # Field name made lowercase.
    is_currently_working = models.BooleanField(db_column='Is_Currently_Working', blank=True,
                                               null=True)  # Field name made lowercase.
    educational_degree = models.TextField(db_column='Educational_Degree', blank=True,
                                          null=True)  # Field name made lowercase.
    graduated_from = models.TextField(db_column='Graduated_From', blank=True, null=True)  # Field name made lowercase.
    graduation_year = models.TextField(db_column='Graduation_Year', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    is_currently_living = models.BooleanField(db_column='Is_Currently_Living', blank=True,
                                              null=True)  # Field name made lowercase.
    topic = models.ForeignKey(TopicsMasterTable, models.DO_NOTHING, db_column='Topic_ID', blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_PROFILE TABLE'


class UserQuestionsTable(models.Model):
    user = models.ForeignKey(UserMasterTable, models.DO_NOTHING, db_column='User_ID', blank=True,
                             null=True)  # Field name made lowercase.
    question_id = models.IntegerField(db_column='Question_ID', blank=True, null=True)  # Field name made lowercase.
    topic = models.ForeignKey(TopicsMasterTable, models.DO_NOTHING, db_column='Topic_ID', blank=True,
                              null=True)  # Field name made lowercase.
    answer = models.ForeignKey(UserAnswerTable, models.DO_NOTHING, db_column='Answer_ID', blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_QUESTIONS TABLE'


class UserSessionTable(models.Model):
    user = models.ForeignKey(UserMasterTable, models.DO_NOTHING, db_column='User_ID', blank=True,
                             null=True)  # Field name made lowercase.
    session_id = models.IntegerField(db_column='Session_ID')  # Field name made lowercase.
    session_start = models.DateTimeField(db_column='Session_Start', blank=True, null=True)  # Field name made lowercase.
    session_end = models.DateTimeField(db_column='Session_End', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_SESSION TABLE'


class UserTopicTable(models.Model):
    user = models.ForeignKey(UserMasterTable, models.DO_NOTHING, db_column='User_ID', blank=True,
                             null=True)  # Field name made lowercase.
    topic = models.ForeignKey(TopicsMasterTable, models.DO_NOTHING, db_column='Topic_ID', blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_TOPIC TABLE'


class VoteMasterTable(models.Model):
    vote_id = models.IntegerField(db_column='Vote_ID', primary_key=True)  # Field name made lowercase.
    vote_type = models.TextField(db_column='Vote_Type', blank=True,
                                 null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'VOTE_MASTER TABLE'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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
