# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('user_passwd', models.CharField(max_length=40)),
                ('user_mail', models.CharField(max_length=30)),
                ('consignee_name', models.CharField(default=b'', max_length=20)),
                ('consignee_address', models.CharField(default=b'', max_length=20)),
                ('consignee_postcode', models.CharField(default=b'', max_length=20)),
                ('consignee_tel', models.CharField(default=b'', max_length=20)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
