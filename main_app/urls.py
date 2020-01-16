from django.urls import path

from . import views

urlpatterns = [
    # years - CRUD
    path("years/", views.YearList.as_view(), name="years - list"),
    path("years/<int:pk>/view/", views.YearDetail.as_view(), name="year - detail"),
    path("years/<int:pk>/edit/", views.YearUpdate.as_view(), name="year - update"),
    path("years/new/", views.YearCreate.as_view(), name="year - create"),
    # groups - CRUD
    path("groups/", views.GroupList.as_view(), name="groups - list"),
    path("groups/<int:pk>/view/", views.GroupDetail.as_view(), name="group - detail"),
    path("groups/<int:pk>/edit/", views.GroupUpdate.as_view(), name="group - update"),
    path("groups/new/", views.GroupCreate.as_view(), name="group - create"),
]
