from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView

from main_app.forms import LoginForm, SignUpForm
from main_app.helpers import LogoutRequiredMixin


class LoginView(LogoutRequiredMixin, FormView):
    """Login View"""

    model = User
    form_class = LoginForm
    template_name = "main_app/auth/login.html"
    success_url = "."

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request=request, username=data["username"], password=data["password"],
            )
            if user:
                login(self.request, user)
                return self.form_valid(form)
            form.errors[NON_FIELD_ERRORS] = form.error_class(
                ["Unable to login with given credentials."]
            )
        return self.form_invalid(form)


class SignUpView(LogoutRequiredMixin, FormView):
    """SignUp View"""

    model = User
    form_class = SignUpForm
    template_name = "main_app/auth/signup.html"
    success_url = "."

    def form_valid(self, form):
        data = form.cleaned_data
        user = self.model.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password"],
            first_name=data["first_name"],
            last_name=data["last_name"],
        )
        login(self.request, user)
        return super(SignUpView, self).form_valid(form)


class HomeView(LoginRequiredMixin, TemplateView):
    """Home/Dashboard View"""

    template_name = "main_app/auth/home.html"


def logout_view(request):
    """logout view."""
    logout(request)
    return redirect(settings.LOGIN_URL)
