from .base import BaseWidget
from calendarApp.models import GroceryItem

class GroceryListWidget(BaseWidget):
    name = "groceryList"
    template_name = "calendarApp/widgets/groceryList.html"

    def get_context_data(self, user=None, config=None):
        items = GroceryItem.objects.filter(user=user).order_by('-added_at')
        return {"items": items}