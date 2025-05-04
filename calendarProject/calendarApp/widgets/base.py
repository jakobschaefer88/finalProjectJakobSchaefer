from abc import ABC, abstractmethod
from django.apps import config
from django.http import request
from django.template.loader import render_to_string

class BaseWidget(ABC):
    name = None
    template_name = None

    def __init__(self, config=None):
        self.config = config or {}

    @abstractmethod
    def get_context_data(self, user=None, config=None):
        return {}

    def render(self, user=None, config=None, request=None):
        context = self.get_context_data(user=user, config=config, request=request)
        if request:
            context["request"] = request  # Needed for csrf_token and user context
        return render_to_string(self.template_name, context)