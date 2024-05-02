from django.urls import path
from purchase_orders import views

urlpatterns = [
    path('purchase_orders/', views.create_list_purchase_orders, name='create_list_purchase_orders'),
    path('purchase_orders/<int:po_id>/', views.retrieve_update_delete_purchase_order, name='retrieve_update_delete_purchase_order'),
    path('vendors/<int:vendor_id>/performance/', views.vendor_performance, name='vendor_performance'),
   
]
