# Generated by Django 2.2 on 2019-04-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unplugged', '0002_simpleadminplugin_simpleadmintemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleadminplugin',
            name='display_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
