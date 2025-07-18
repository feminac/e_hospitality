# Generated by Django 5.2 on 2025-06-30 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MedicalHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("diagnosis", models.TextField()),
                ("medications", models.TextField(blank=True)),
                ("allergies", models.TextField(blank=True)),
                ("treatment", models.TextField(blank=True)),
                ("date_recorded", models.DateField(auto_now_add=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medical_history",
                        to="patients.patient",
                    ),
                ),
            ],
        ),
    ]
