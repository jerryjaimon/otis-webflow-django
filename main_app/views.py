from django.urls import get_resolver
from django.shortcuts import render

def index_page(request):
    return render(request, 'detail_client.html')

def asset_page(request):
    return render(request, 'detail_asset.html')

def report_page(request):
    return render(request, 'detail_reports.html')