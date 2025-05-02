from django.shortcuts import render
from .widgets import registry
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GroceryItem
from .forms import GroceryItemForm

def dashboard(request):
    user = request.user if request.user.is_authenticated else None

    # Load all registered widgets
    rendered_widgets = []
    for widget_class in registry:
        widget = widget_class()
        html = widget.render(user=user)
        rendered_widgets.append(html)

    context = {
        "rendered_widgets": rendered_widgets
    }

    return render(request, "calendarApp/dashboard.html", context)

@csrf_exempt
def grocery_list_view(request):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    if request.method == "POST":
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = user
            item.save()
            return JsonResponse({"success": True, "item": item.name})
        return JsonResponse({"success": False, "errors": form.errors})

    elif request.method == "GET":
        items = GroceryItem.objects.filter(user=user).values("id", "name", "completed")
        return JsonResponse(list(items), safe=False)