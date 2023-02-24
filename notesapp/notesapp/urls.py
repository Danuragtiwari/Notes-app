"""notesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from account import views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/signup/', views.signup, name='signup'),
    path('account/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('account/logout/', views.logout_view, name='logout'),
    path('account/change_password/', views.change_password, name='change_password'),
    path('account/', include('django.contrib.auth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('notes.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
