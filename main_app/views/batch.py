from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from main_app.forms import BatchForm
from .base import AbstractAuthenticatedView
from ..models import Batch


class BatchView(AbstractAuthenticatedView):
    form_class = BatchForm
    success_url = "/batches"
    model = Batch
    queryset = Batch.objects.all()


class BatchCreate(BatchView, CreateView):
    template_name = "main_app/batch/create.html"


class BatchDetail(BatchView, DetailView):
    template_name = "main_app/batch/detail.html"


class BatchList(BatchView, ListView):
    template_name = "main_app/batch/list.html"


class BatchUpdate(BatchView, UpdateView):
    template_name = "main_app/batch/update.html"


class BatchDelete(BatchView, DeleteView):
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
