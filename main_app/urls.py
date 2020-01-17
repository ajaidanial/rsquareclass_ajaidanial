from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # auth views
    path("", RedirectView.as_view(url="/login"), name="login view"),
    path("login/", views.LoginView.as_view(), name="login view"),
    path("signup/", views.SignUpView.as_view(), name="signup view"),
    path("home/", views.HomeView.as_view(), name="home view"),
    path("logout/", views.logout_view, name="logout"),
    # years - CRUD
    path("years/", views.YearList.as_view(), name="years - list"),
    path("years/<int:pk>/view/", views.YearDetail.as_view(), name="year - detail"),
    path("years/<int:pk>/edit/", views.YearUpdate.as_view(), name="year - update"),
    path("years/<int:pk>/delete/", views.YearDelete.as_view(), name="year - delete"),
    path("years/new/", views.YearCreate.as_view(), name="year - create"),
    # groups - CRUD
    path("groups/", views.GroupList.as_view(), name="groups - list"),
    path("groups/<int:pk>/view/", views.GroupDetail.as_view(), name="group - detail"),
    path("groups/<int:pk>/edit/", views.GroupUpdate.as_view(), name="group - update"),
    path("groups/<int:pk>/delete/", views.GroupDelete.as_view(), name="group - delete"),
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
    path(
        "subjects/<int:pk>/delete/",
        views.SubjectDelete.as_view(),
        name="subject - delete",
    ),
    path("subjects/new/", views.SubjectCreate.as_view(), name="subject - create"),
    # batches - CRUD
    path("batches/", views.BatchList.as_view(), name="batches - list"),
    path("batches/<int:pk>/view/", views.BatchDetail.as_view(), name="batch - detail"),
    path("batches/<int:pk>/edit/", views.BatchUpdate.as_view(), name="batch - update"),
    path(
        "batches/<int:pk>/delete/", views.BatchDelete.as_view(), name="batch - delete"
    ),
    path("batches/new/", views.BatchCreate.as_view(), name="batch - create"),
]
