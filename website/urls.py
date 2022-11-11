from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.apps.public.urls')),
    path('accounts/', include('website.apps.accounts.urls')),

]

