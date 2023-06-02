# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    plan = models.CharField(max_length=255, null=True, blank=True)
    attribute_1 = models.CharField(max_length=255, null=True, blank=True)
    attribute_2 = models.CharField(max_length=255, null=True, blank=True)
    attribute_3 = models.CharField(max_length=255, null=True, blank=True)
    attribute_4 = models.CharField(max_length=255, null=True, blank=True)
    attribute_5 = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Channel(models.Model):

    #__Channel_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    sync_status = models.CharField(max_length=255, null=True, blank=True)
    attribute_1 = models.CharField(max_length=255, null=True, blank=True)
    attribute_2 = models.CharField(max_length=255, null=True, blank=True)
    attribute_3 = models.CharField(max_length=255, null=True, blank=True)
    attribute_4 = models.CharField(max_length=255, null=True, blank=True)
    attribute_5 = models.CharField(max_length=255, null=True, blank=True)

    #__Channel_FIELDS__END

    class Meta:
        verbose_name        = _("Channel")
        verbose_name_plural = _("Channel")



#__MODELS__END
