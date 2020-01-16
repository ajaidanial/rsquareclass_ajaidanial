from django.apps import apps
from django.contrib import admin
from django.contrib.auth import get_user_model

# Register User model
try:
    User = get_user_model()
    admin.site.register(User)
except admin.sites.AlreadyRegistered:
    pass

# Register all other models
models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
