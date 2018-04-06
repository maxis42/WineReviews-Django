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
    url('^wine/(?P<wine_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    # ex: /review/user - get reviews for the logged user
    url('^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url('^review/user/$', views.user_review_list, name='user_review_list'),
]
