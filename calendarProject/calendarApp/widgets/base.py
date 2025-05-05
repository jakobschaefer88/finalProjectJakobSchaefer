'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Base.py file

'''

from abc import ABC, abstractmethod
from django.template.loader import render_to_string

#base class for all the widgets
class BaseWidget(ABC):
    name = None
    template_name = None

    # Initializes the widget
    def __init__(self, config=None):
        self.config = config or {}

    #Abstract methon that gets implemented by each widget
    @abstractmethod
    def get_context_data(self, user=None, config=None):
        return {}

    #renders the widget by passing the context to the template
    def render(self, user=None, config=None, request=None):
        context = self.get_context_data(user=user, config=config, request=request)
        if request:
            context["request"] = request  # Needed for csrf_token and user context
        return render_to_string(self.template_name, context)