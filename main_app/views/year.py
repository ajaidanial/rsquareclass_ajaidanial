from django.views.generic import CreateView, DetailView, ListView, UpdateView

from main_app.forms import YearForm
from .base import AbstractAuthenticatedView
from ..models import Year


class YearView(AbstractAuthenticatedView):
    form_class = YearForm
    success_url = "."
    model = Year
    queryset = Year.objects.all()


class YearCreate(YearView, CreateView):
    template_name = "main_app/year/create.html"


class YearDetail(YearView, DetailView):
    template_name = "main_app/year/detail.html"


class YearList(YearView, ListView):
    template_name = "main_app/year/list.html"


class YearUpdate(YearView, UpdateView):
    template_name = "main_app/year/update.html"
