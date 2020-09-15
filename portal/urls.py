from django.urls import path
# so file can access functions written in views.py that handle HTTP responses, validation, etc!
from . import views

urlpatterns = [
    # home page url pattern
    # url  is "" (empty string) and is handled by the 'home' func from views.py
    path('', views.home, name='portal-home'),

    # about page url pattern
    # url is "/aboutme" and is handled by the 'about' func from views.py
    path('aboutme/', views.about, name='portal-about'),

    # github page url pattern
    # url is "/github" and is handled by 'github' func from views.py
    path('githubprojects/', views.github, name='portal-github'),
]
