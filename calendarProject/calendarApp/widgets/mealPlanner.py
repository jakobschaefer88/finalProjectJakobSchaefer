import datetime
from .base import BaseWidget

class MealPlannerWidget(BaseWidget):
    name = 'mealPlanner'
    template_name = "calendarApp/widgets/mealPlanner.html"

    def get_context_data(self, user=None, config=None):
        today = datetime.date.today()

        # Placeholder: meal will be pulled from the database in the future
        meal = None

        return {
            "date": today.strftime("%B %d, %Y"),
            "meal": meal
        }