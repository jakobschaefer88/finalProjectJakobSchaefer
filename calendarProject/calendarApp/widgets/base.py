from abc import ABC, abstractmethod

class BaseWidget(ABC):
    name = None  # e.g. "weather", "news"
    template_name = None  # e.g. "calendarApp/widgets/weather.html"

    def __init__(self, config=None):
        self.config = config or {}

    @abstractmethod
    def get_context_data(self, user=None, config=None):
        """Return context data passed to the widget template."""
        return {}

    def render(self, user=None):
        """Use Django's rendering engine to render the widget."""
        from django.template.loader import render_to_string
        return render_to_string(self.template_name, self.get_context_data(user, self.config))