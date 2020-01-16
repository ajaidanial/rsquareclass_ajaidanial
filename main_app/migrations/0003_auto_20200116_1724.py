# Generated by Django 3.0.2 on 2020-01-16 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_group_subject_year"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="group", options={"ordering": ["-standard", "name"]},
        ),
        migrations.AlterModelOptions(name="subject", options={"ordering": ["name"]},),
        migrations.AlterModelOptions(
            name="year", options={"ordering": ["-from_year", "to_year"]},
        ),
        migrations.CreateModel(
            name="Batch",
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
                ("name", models.CharField(max_length=50)),
                (
                    "subjects",
                    models.ManyToManyField(
                        related_name="batches", to="main_app.Subject"
                    ),
                ),
                (
                    "year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="batches",
                        to="main_app.Year",
                    ),
                ),
            ],
            options={"ordering": ["name"],},
        ),
    ]
