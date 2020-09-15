"""PersonalWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

# These urlpatterns are communicating with the urlpatterns in portal/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    # telling django to use portal.urls to serve webpage
    # This acts as the beginning portion of the url. We specify the differnt subpages in the portal/urls.py
    # By using empty string as our url-prefixer, we can simply go to urls such as localhost:8000/aboutme, /githubprojects
    path("", include('portal.urls'))

]
