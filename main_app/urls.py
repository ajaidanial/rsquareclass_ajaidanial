from django.urls import path

from . import views

urlpatterns = [
    # years - CRUD
    path("years/", views.YearList.as_view(), name="years - list"),
    path("years/<int:pk>/view/", views.YearDetail.as_view(), name="year - detail"),
    path("years/<int:pk>/edit/", views.YearUpdate.as_view(), name="year - update"),
    path("years/new/", views.YearCreate.as_view(), name="year - create"),
]
