"""This file loads the initial data into the database on `migrate`."""
from django.contrib.auth import get_user_model
from django.db import migrations

from rsquareclass_task1.settings import ADMIN_USER

# get the base user for tha project
User = get_user_model()


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
    operations = [
        migrations.RunPython(create_super_user, reverse_code=delete_super_user),
    ]
