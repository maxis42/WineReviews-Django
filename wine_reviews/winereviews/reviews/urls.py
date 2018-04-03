from django.conf.urls import url
from . import views

app_name = 'reviews'
urlpatterns = [
    # ex: /
    url('^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url('^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    url('^wine$', views.wine_list, name='wine_list'),
    # ex: /wine/5/
    url('^wine/(?P<wine_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),
    url(r'^wine/(?P<wine_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]
