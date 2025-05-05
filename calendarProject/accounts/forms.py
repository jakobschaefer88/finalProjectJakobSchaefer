'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Forms File

'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Define a class using Django's UserCreation form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True) # required email field

    class Meta:
        model = User # confirms this form is tied to the User model
        #Fields that appear on the registration form
        fields = ['username', 'email', 'password1', 'password2']
