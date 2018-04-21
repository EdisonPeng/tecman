from django.conf.urls import url

from . import views

app_name = 'erp'
urlpatterns = [
    url(r'^account_index/$', views.account_index, name='account_index'),
    url(r'^account_index/(?P<account_id>[0-9]+)/$', views.account_detail, name='account_detail'),
    url(r'^account_index/transfer/$', views.transfer, name='transfer'),
    url(r'^account_index/execute_transfer/$', views.execute_transfer, name='execute_transfer'),
]
