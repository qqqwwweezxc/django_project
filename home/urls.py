from django.urls import path, re_path
from .views import (
    home, about, contact, post_view, profile_view, event_view,
    version_product, blog, order, report)


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    re_path(r'^post/(\d+)/$', post_view),
    re_path(r'^profile/([a-zA-Z]+)/$', profile_view),
    re_path(r'^event/(\d{4})/(\d{2})/(\d{2})/$', event_view),
    re_path(r'^release/v(\d{1,2})$', version_product),
    re_path(r'^blog/(\d{4})/(\d{2})$', blog),
    re_path(r'^order/([A-Z]{2}\d{4})$', order),
    re_path(r'^report/([a-zA-Z]+)(?:\.(pdf|csv))?$', report),
]

