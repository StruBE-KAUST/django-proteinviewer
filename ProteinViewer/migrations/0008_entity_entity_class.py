# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-28 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProteinViewer', '0007_auto_20170928_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='entity_class',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
