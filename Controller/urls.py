from django.urls import path
from .views import admin_dashboard_view


urlpatterns = [
    path('adminDashboard', admin_dashboard_view, name="admin_dashboard_view")
]
