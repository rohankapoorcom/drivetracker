# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drives', '0003_alter_capacity_to_be_nullable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harddrive',
            name='in_use',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='harddrive',
            name='purchase_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='harddrive',
            name='service_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='harddrive',
            name='service_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='harddrive',
            name='status',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='harddrive',
            name='warranty_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]