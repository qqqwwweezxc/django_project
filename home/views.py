from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    """Render the home page."""
    return render(request, 'home/home.html')


def about(request: HttpRequest) -> HttpResponse:
    """Render the about page."""
    return render(request, 'home/about.html')


def contact(request: HttpRequest) -> HttpResponse:
    """Render the contact page."""
    return render(request, 'home/contact.html')


def post_view(request: HttpRequest, id: int) -> HttpResponse:
    """Displays a post by id."""
    return render(request, 'home/post.html', {'id': id})


def profile_view(request: HttpRequest, username: str) -> HttpResponse:
    """Displays a profile by username."""
    return render(request, 'home/profile.html', {'username': username})


def event_view(request: HttpRequest, year: int, month: int, day: int) -> HttpResponse:
    """Displays event by date."""
    return render(request, 'home/event.html', {
        'year': year,
        'month': month,
        'day': day
    })


def version_product(request: HttpRequest, version: str) -> HttpResponse:
    """Displays product version."""
    return render(request, 'home/version.html', {'version': version})


def blog(request: HttpRequest, year: int, month: int) -> HttpResponse:
    """Displays blog page by date."""
    return render(request, 'home/blog.html', {'year': year, 'month': month})


def order(request: HttpRequest, order_id: int) -> HttpResponse:
    """Displays oder by order id."""
    return render(request, 'home/order.html', {'order_id': order_id})


def report(request: HttpRequest, slug: str, ext: str = None) -> HttpResponse:
    """Displays report."""
    return render(request, 'home/report.html', {'slug': slug, 'ext': ext})