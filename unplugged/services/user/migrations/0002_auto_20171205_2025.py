# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 20:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("services_user", "0001_initial")]

    operations = [
        migrations.AlterUniqueTogether(name="userinfo", unique_together=set([])),
        migrations.RemoveField(model_name="userinfo", name="user"),
        migrations.DeleteModel(name="Userinfo"),
    ]