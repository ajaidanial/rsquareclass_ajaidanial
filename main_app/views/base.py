from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View


class AbstractAuthenticatedView(LoginRequiredMixin, View):
    """The base for all views that are authenticated"""

    class Meta:
        abstract = True
