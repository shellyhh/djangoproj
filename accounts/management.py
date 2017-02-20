#-*- coding:utf8 -*-

from django.contrib.auth.models import User

#创建超级用户
def create_superuser(signal, sender, **kwargs):

    if User in (v for k, v in sender.models.iteritems()):
        admin = User.objects.filter(username='admin')
        if not admin:
            User.objects.create_superuser('admin', 'admin@qq.com', 'admin')

