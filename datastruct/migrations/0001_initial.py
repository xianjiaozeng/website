# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=100)),
                ('SubItemName', models.CharField(max_length=100)),
                ('UnitName', models.CharField(max_length=50)),
                ('Weight', models.IntegerField()),
                ('MaxSingle', models.IntegerField()),
            ],
        ),
    ]
