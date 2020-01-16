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
    # subjects - CRUD
    path("subjects/", views.SubjectList.as_view(), name="subjects - list"),
    path(
        "subjects/<int:pk>/view/",
        views.SubjectDetail.as_view(),
        name="subject - detail",
    ),
    path(
        "subjects/<int:pk>/edit/",
        views.SubjectUpdate.as_view(),
        name="subject - update",
    ),
    path("subjects/new/", views.SubjectCreate.as_view(), name="subject - create"),
]
