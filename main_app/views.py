from django.urls import get_resolver
from django.shortcuts import render
from main_app.models import Application  # Import the Application model


def index_page(request):
    applications = Application.objects.all()
    return render(request, 'detail_client.html', {'applications': applications})

def asset_page(request):
    return render(request, 'detail_asset.html')

def report_page(request):
    return render(request, 'detail_reports.html')



