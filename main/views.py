from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


class ContactView(TemplateView):
    template_name = "main/contact.html"


class ServiceView(TemplateView):
    template_name = "main/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        services_list = [
            {"title": "Web Development", "description": "Creating modern websites"},
            {"title": "UI/UX Design", "description": "User-friendly interfaces"},
            {"title": "Backend Development", "description": "Server-side logic"},
            {"title": "API Integration", "description": "Connecting services"},
            {"title": "Support", "description": "Technical help"},
        ]

        query = self.request.GET.get("q", "").lower()

        if query:
            services_list = [
                s for s in services_list
                if query in s["title"].lower() or query in s["description"].lower()
            ]

        context["services"] = services_list
        context["query"] = query

        return context



