from django.views.generic import CreateView, DetailView, ListView, UpdateView

from main_app.forms import SubjectForm
from .base import AbstractAuthenticatedView
from ..models import Subject


class SubjectView(AbstractAuthenticatedView):
    form_class = SubjectForm
    success_url = "."
    model = Subject
    queryset = Subject.objects.all()


class SubjectCreate(SubjectView, CreateView):
    template_name = "main_app/subject/create.html"


class SubjectDetail(SubjectView, DetailView):
    template_name = "main_app/subject/detail.html"


class SubjectList(SubjectView, ListView):
    template_name = "main_app/subject/list.html"


class SubjectUpdate(SubjectView, UpdateView):
    template_name = "main_app/subject/update.html"
