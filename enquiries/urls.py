
from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_enquiry, name='submit_enquiry'),
    path('admin-login/', views.admin_login ,name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard,name='admin_dashboard'),
    path('enquiry/<int:enquiry_id>/',views.enquiry_detail,name='enquiry_detail'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('customer-enquiries/',views.customer_enquiries,name='customer_enquiries'),
]
