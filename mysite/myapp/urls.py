from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=LoginForm)),
    path('dashboard/',  views.dashboard),
    path('submit', views.submit),
    path('newwhiteboard/', views.create_whiteboard),
    path('whiteboard/', views.whiteboard),
    path('logout/', views.logout_view),
    path('profile/' , views.profile),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

