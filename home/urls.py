from django.urls import path, re_path
from .views import home, about, contact, post_view, profile_view, event_view


urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
    re_path(r'^post/(\d+)/$', post_view),
    re_path(r'^profile/([a-zA-Z]+)/$', profile_view),
    re_path(r'^event/(\d{4})/(\d{2})/(\d{2})/$', event_view),

]

