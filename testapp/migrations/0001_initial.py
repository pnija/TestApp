# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_id', models.IntegerField(null=True, blank=True)),
                ('client_id', models.IntegerField(null=True, blank=True)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
