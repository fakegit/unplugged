# Generated by Django 2.2 on 2019-07-06 08:17

import django.db.models.deletion
import jsonfield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("unplugged", "0006_auto_20190522_1907"),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action", models.CharField(db_index=True, max_length=50)),
                ("start_datetime", models.DateTimeField(auto_now_add=True)),
                ("end_datetime", models.DateTimeField(null=True)),
                ("progress", models.PositiveIntegerField(default=0)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("ongoing", "Ongoing"),
                            ("success", "Success"),
                            ("failed", "Failed"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="pending",
                        max_length=12,
                    ),
                ),
                (
                    "plugin",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="unplugged.Plugin",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="schedule",
            name="kwargs",
            field=jsonfield.fields.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="plugin_unique_id",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.CreateModel(
            name="LogMessage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("msg", models.TextField(blank=True, default="")),
                (
                    "log",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="unplugged.Log"
                    ),
                ),
            ],
        ),
    ]
