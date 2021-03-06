from django.urls import path
from . import views
app_name = 'CUSTOMERS'

urlpatterns = [
    # path('',views.customer_list,name='customer'),
    path('list/', views.customer_list, name='customer_list'),
    path('history/',views.history,name='history'),
    path('profile/<int:cust_id>',views.profile,name='profile'),
    path('message/',views.messages_pages,name='message')
]