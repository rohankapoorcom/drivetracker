# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drives', '0010_linking_up_new_foreignkeys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='harddrive',
            name='host'
        ),
        migrations.RemoveField(
            model_name='harddrive',
            name='manufacturer'
        ),
        migrations.RemoveField(
            model_name='harddrive',
            name='model'
        ),
        migrations.RenameField(
            model_name='harddrive',
            old_name='host_new',
            new_name='host'
        ),
        migrations.RenameField(
            model_name='harddrive',
            old_name='manufacturer_new',
            new_name='manufacturer'
        ),
        migrations.RenameField(
            model_name='harddrive',
            old_name='model_new',
            new_name='model'
        ),
    ]
