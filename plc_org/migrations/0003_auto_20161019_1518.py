# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plc_org', '0002_controller_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='equipment_description',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_id',
            field=models.CharField(max_length=255),
        ),
    ]