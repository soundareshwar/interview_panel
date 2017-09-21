# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel_inter_app', '0003_dummy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule_Inter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Dummy',
        ),
    ]
