from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('profile/', views.profile_page, name='profile'),
    path('setting/', views.ProfileSettingView.as_view(), name='setting'),
    path('login/', auth_views.LoginView.as_view(extra_context={'pagename': 'Авторизация'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("register/", RegistrationView.as_view(extra_context={'pagename': 'Регистрация'}),
         name="django_registration_register",),
    path("register/complete/", TemplateView.as_view(template_name="django_registration/registration_complete.html",
                                                    extra_context={'pagename': 'Регистрация'}),
         name="django_registration_complete",),
]
