# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial01'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='user_mail',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='user_passwd',
            field=models.CharField(max_length=40),
        ),
    ]
