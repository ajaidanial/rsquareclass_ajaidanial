from django.views.generic.base import View


class AbstractAuthenticatedView(View):
    """The base for all views that are authenticated"""

    class Meta:
        abstract = True


# TODO: look into this file
