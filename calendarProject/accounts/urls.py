'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Urls File

'''

from . import views
from django.urls import path

#Define the namespace for this apps URLS
app_name = "accounts"

urlpatterns = [
    #URL Pattern for registering a new user
    path("register/", views.register_view, name="register"),
    #URL pattern for logging in a user
    path("login/", views.login_view, name="login"),
    #URL pattern for logging out a user
    path("logout/", views.logout_view, name="logout"),
]