from django.urls import path
from . import views

urlpatterns = [
    # ... Your existing URL patterns ...
    path('', views.index_page, name='index_page'),
    path('asset/', views.asset_page, name='asset_page'),
    path('report/', views.report_page, name='report_page'),

]
