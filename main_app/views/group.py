from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from main_app.forms import GroupForm
from .base import AbstractAuthenticatedView
from ..models import Group


class GroupView(AbstractAuthenticatedView):
    form_class = GroupForm
    success_url = "/groups"
    model = Group
    queryset = Group.objects.all()


class GroupCreate(GroupView, CreateView):
    template_name = "main_app/group/create.html"


class GroupDetail(GroupView, DetailView):
    template_name = "main_app/group/detail.html"


class GroupList(GroupView, ListView):
    template_name = "main_app/group/list.html"


class GroupUpdate(GroupView, UpdateView):
    template_name = "main_app/group/update.html"


class GroupDelete(GroupView, DeleteView):
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
