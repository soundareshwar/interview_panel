# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel_inter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel_inter',
            name='outstation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='panel_inter',
            name='weekend',
            field=models.BooleanField(default=False),
        ),
    ]
