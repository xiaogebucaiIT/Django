from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Host(models.Model):
    hostname = models.CharField(max_length=64, unique=True)
    ip_addr = models.GenericIPAddressField(unique=True)
    port = models.IntegerField(default=22)

    system_type_choices = (
        ('linux', 'LINUX'),
        ('win32', 'WINDOWS'),
    )
    system_type = models.CharField(choices=system_type_choices, max_length=32)
    enabled = models.BooleanField(default=True)

    create_date = models.DateTimeField(auto_now_add=True)
    online_date = models.DateTimeField()

    gruops = models.ManyToManyField('HostGroup')
    idc = models.ForeignKey('IDC')

    def __unicode__(self):
        return self.hostname


class IDC(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name


class HostGroup(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64, unique=True)
    host_groups = models.ManyToManyField('HostGroup', blank=True, null=True)
    host = models.ManyToManyField('Host', blank=True, null=True)

    def __unicode__(self):
        return self.name












