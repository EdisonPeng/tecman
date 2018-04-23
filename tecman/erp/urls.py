from django.conf.urls import url

from . import views

app_name = 'erp'
urlpatterns = [
    url(r'^account_index/$', views.account_index, name='account_index'),
    url(r'^account_index/(?P<account_id>[0-9]+)/$', views.account_detail,
        name='account_detail'),
    url(r'^account_index/transfer/$', views.transfer, name='transfer'),
    url(r'^operating_expense_index/$', views.operating_expense_index,
        name='operating_expense_index'),
    url(r'^operating_expense_index/(?P<operating_expense_id>[0-9]+)/$',
        views.operating_expense_detail, name='operating_expense_detail'),
    url(r'^operating_expense_index/create_operating_expense/$',
        views.create_operating_expense, name='create_operating_expense'),
]
