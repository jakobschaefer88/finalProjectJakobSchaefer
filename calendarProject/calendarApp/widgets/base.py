class BaseWidget:
    name = "Base"
    templateName = "calendarApp/widgets/base.html"

    def get_context_data(self, user=None, config=None):
        return{}
