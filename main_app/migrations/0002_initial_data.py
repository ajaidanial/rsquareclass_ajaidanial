"""This file loads the initial data into the database on `migrate`."""
import os

from django.contrib.auth import get_user_model
from django.core import serializers
from django.db import migrations

from rsquareclass_task1.settings import ADMIN_USER, BASE_DIR

# get the base user for tha project
User = get_user_model()

# for fixtures
fixture_dir = os.path.join(BASE_DIR, "main_app/fixtures")
fixture_files = ["years.yaml", "groups.yaml", "subjects.yaml"]
fixture_models = ["Year", "Group", "Subject"]


def load_fixtures(apps, schema_editor):
    # load fixtures
    for name in fixture_files:
        fixture_file = os.path.join(fixture_dir, name)
        fixture = open(fixture_file, "rb")
        objects = serializers.deserialize("yaml", fixture, ignorenonexistent=True)
        for object in objects:
            object.save()
        fixture.close()


def unload_fixtures(apps, schema_editor):
    # unload fixtures
    for model in fixture_models:
        ModelClass = apps.get_model("main_app", model)
        ModelClass.objects.all().delete()


def create_super_user(apps, schema_editor):
    # create the app super user
    User.objects.create_superuser(
        username=ADMIN_USER["username"],
        email=ADMIN_USER["username"],
        password=ADMIN_USER["password"],
        first_name="Admin",
        last_name="User",
    )


def delete_super_user(apps, schema_editor):
    # delete the app super user
    User.objects.get(email=ADMIN_USER["username"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_super_user, reverse_code=delete_super_user),
        migrations.RunPython(load_fixtures, reverse_code=unload_fixtures),
    ]
