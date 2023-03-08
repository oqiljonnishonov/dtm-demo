# Generated by Django 4.1.6 on 2023-02-12 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Citizenship",
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
                (
                    "citizens",
                    models.CharField(max_length=100, verbose_name="Citizenship"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InstitutionType",
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
                (
                    "type",
                    models.CharField(max_length=50, verbose_name="Institutions types"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="States",
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
                ("state", models.CharField(max_length=50, verbose_name="States")),
            ],
        ),
        migrations.CreateModel(
            name="Regions",
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
                ("region", models.CharField(max_length=50, verbose_name="Regions")),
                (
                    "states",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base_info.states",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Institutions",
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
                (
                    "institution",
                    models.CharField(
                        max_length=100, verbose_name="Educational Institutions"
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base_info.regions",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base_info.states",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base_info.institutiontype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Districts",
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
                ("district", models.CharField(max_length=20, verbose_name="districts")),
                (
                    "regions",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base_info.regions",
                    ),
                ),
            ],
        ),
    ]