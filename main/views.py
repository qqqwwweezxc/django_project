from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from typing import Any, Dict

def home(request: HttpRequest) -> HttpResponse:
    """Render the home page."""
    return render(request, 'main/home.html')


def about(request: HttpRequest) -> HttpResponse:
    """Render the about page."""
    return render(request, 'main/about.html')


class ContactView(TemplateView):
    """Display contact page."""
    template_name = "main/contact.html"


class ServiceView(TemplateView):
    """Display services with search filtering."""
    template_name = "main/services.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add services list and search query to context."""
        context = super().get_context_data(**kwargs)

        services_list: list[Dict] = [
            {"title": "Web Development", "description": "Creating modern websites"},
            {"title": "UI/UX Design", "description": "User-friendly interfaces"},
            {"title": "Backend Development", "description": "Server-side logic"},
            {"title": "API Integration", "description": "Connecting services"},
            {"title": "Support", "description": "Technical help"},
        ]

        query: str = self.request.GET.get("q", "").lower()

        if query:
            services_list = [
                s for s in services_list
                if query in s["title"].lower() or query in s["description"].lower()
            ]

        context["services"] = services_list
        context["query"] = query

        return context



