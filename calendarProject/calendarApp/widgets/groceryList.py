from .base import BaseWidget
from calendarApp.models import GroceryItem

class GroceryListWidget(BaseWidget):
    name = 'groceryList'
    template_name = "calendarApp/widgets/grocery_list.html"

    def get_context_data(self, user=None, config=None):
        items = []
        if user and user.is_authenticated:
            items = GroceryItem.objects.filter(user=user).order_by('-created_at')
        return {
            "items": items
        }