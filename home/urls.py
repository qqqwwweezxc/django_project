from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    re_path(r'^post/(\d+)/$', views.post_view),
    re_path(r'^profile/([a-zA-Z]+)/$', views.profile_view),
    re_path(r'^event/(\d{4})/(\d{2})/(\d{2})/$', views.event_view),
    re_path(r'^release/v(\d{1,2})$', views.version_product),
    re_path(r'^blog/(\d{4})/(\d{2})$', views.blog),
    re_path(r'^order/([A-Z]{2}\d{4})$', views.order),
    re_path(r'^report/([a-zA-Z]+)(?:\.(pdf|csv))?$', views.report),
]

