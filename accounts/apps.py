#-*- coding:utf8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_migrate
from management import create_superuser

class StadminConfig(AppConfig):
    name = 'accounts'
    verbose_name = _(u"accounts")

    def ready(self):
        post_migrate.connect(create_superuser)
