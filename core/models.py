#PACKAGE IMPORTS
from django.db import models

#LOCAL IMPORTS

class Qodex_users(models.Model):
    """ """
    #RELATED FIELDS
    #qodex_org = models.ForeignKey('Qodex_org', db_column='qodex_org', on_delete=models.SET_NULL, blank=True, null=True)
    #role = models.ForeignKey('User_roles', db_column='user_roles', on_delete=models.SET_NULL, blank=True, null=True)
    #region = models.ForeignKey('Regions', db_column='regions', on_delete=models.SET_NULL, blank=True, null=True)
    #LOCAL FIELDS
    name = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    last_ip = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    weight_fault = models.IntegerField(blank=True, null=True)
    connected = models.BooleanField(blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    def __str__(self):
        """ Django-admin UI """
        return '%s-%s' % (self.name, self.inn)
    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Qodex_user'

class Weight_types(models.Model):
    """ Weight_types - model of weight_types databases """
    def __str__(self):
        return self.name

    #LOCAL FIELDS
    name = models.TextField(blank=True, null=True)    

    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Weight_types'


   
class Operators(models.Model):
    """ Operators - model of operators databases """
    def __str__(self):
        return self.username

#LOCAL FIELDS
    username = models.TextField(blank=True, null=True)  
    password = models.TextField(blank=True, null=True)  
    role = models.CharField(max_length=30, blank=True, null=True)
    fullname = models.CharField(max_length=30, blank=True, null=True)
    ex_id = models.IntegerField(blank=True, null=True)
    upd_time = models.DateTimeField(blank=True, null=True)
    ar_get = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

#RELATED FIELDS
    poligon = models.ForeignKey('Qodex_Users', db_column='poligon', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Operators'

class Qodex_achive(models.Model):
    """ Qodex_achive - model of qodex_achive databases """
    def __str__(self):
        return self.user

#LOCAL FIELDS
    date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=20, blank=True, null=True)
    origin = models.TextField(blank=True, null=True) 
    new_data = models.TextField(blank=True, null=True) 
    restored = models.BooleanField(blank=True, null=True)
    restored_date = models.DateTimeField(blank=True, null=True)

#RELATED FIELDS
    #table = models.ForeignKey('Qodex_Users', db_column='table', on_delete=models.SET_NULL, blank=True, null=True)
    poligon = models.ForeignKey('Qodex_users', db_column='poligon', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Qodex_achive'

class Cm_events_log(models.Model):
    """ Cm_events_log - model of m_events_log databases """
    def __str__(self):
        return self.operator

#LOCAL FIELDS
    datetime = models.DateTimeField(blank=True, null=True)
    event = models.IntegerField(blank=True, null=True)
    operator = models.CharField(max_length=12, blank=True, null=True)
    ex_id = models.IntegerField(blank=True, null=True)
    upd_time = models.DateTimeField(blank=True, null=True)
#RELATED FIELDS
    poligon = models.ForeignKey('Qodex_users', db_column='poligon', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        """ Model configurations """
        managed = True
        db_table = 'Cm_events_log'

