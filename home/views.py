from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def post_view(request, id):
    return render(request, 'home/post.html', {'id': id})


def profile_view(request, username):
    return render(request, 'home/profile.html', {'username': username})


def event_view(request, year, month, day):
    return render(request, 'home/event.html', {
        'year': year,
        'month': month,
        'day': day
    })


def version_product(request, version):
    return render(request, 'home/version.html', {'version': version})


def blog(request, year, month):
    return render(request, 'home/blog.html', {'year': year, 'month': month})


def order(request, order_id):
    return render(request, 'home/order.html', {'order_id': order_id})


def report(request, slug, ext: None):
    return render(request, 'home/report.html', {'slug': slug, 'ext': ext})