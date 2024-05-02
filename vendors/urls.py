from django.urls import path
from vendors import views

urlpatterns = [
    path('signup/', views.signup, name='signup_api'),
    path('login/', views.login, name='login_api'),
    path('logout/', views.logout, name='logout_api'),
    path('vendors/', views.vendors, name='list_create_vendors'),
    path('vendors/<int:vendor_id>/', views.retrieve_update_delete_vendor, name='retrieve_update_delete_vendor'),
]
