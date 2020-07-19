from django.urls import path
from . import views

urlpatterns = [
    path('',views.customer_form,name='customer_insert'),
    path('<int:id>/',views.customer_form,name='update_customer'),
    path('list/',views.customer_list,name='customer_list'),
    path('individual/<int:id>/',views.individual_customer,name='individual'),
    path('delete/<int:id>/',views.customer_delete,name='delete_customer'),
]