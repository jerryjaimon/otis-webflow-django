from django.urls import get_resolver
from django.shortcuts import render
from main_app.models import Application,Scan  # Import the Application model
from datetime import date  # Import the date module


def index_page(request):
    applications = Application.objects.all()
    return render(request, 'detail_client.html', {'applications': applications})

def asset_page(request,slug):
    try:
        application = Application.objects.get(app_slug=slug)
        app_hash = application.app_hash
        scans = Scan.objects.filter(app_hash=app_hash)
        context = {'scans': scans}
    except Application.DoesNotExist:
        # Handle the case where the application with the given slug does not exist
        return None
    return render(request, 'detail_asset.html',context)

def report_page(request):
    scan_data()
    return render(request, 'detail_reports.html')



def scan_data():
    new_scan1 = Scan(
        scan_slug='scan1',
        scan_status='SCAN_COMPLETED',
        scan_created=date.today(),
        scan_start=date.today(),
        scan_end=date.today(),
        static_scan_status='SCAN_COMPLETED',
        static_scan_start=date.today(),
        static_scan_end=date.today(),
        dynamic_scan_status='SCAN_COMPLETED',
        dynamic_scan_start=date.today(),
        dynamic_scan_end=date.today(),
        api_scan_status='SCAN_COMPLETED',
        api_scan_start=date.today(),
        api_scan_end=date.today(),
        app_hash='hash1',
        modified_app_hash='hashh1',
        score=50,  # Replace with an actual score
        file_path='your_file_path',
    )

    new_scan2 = Scan(
        scan_slug='scan2',
        scan_status='SCAN_COMPLETED',
        scan_created=date.today(),
        scan_start=date.today(),
        scan_end=date.today(),
        static_scan_status='SCAN_COMPLETED',
        static_scan_start=date.today(),
        static_scan_end=date.today(),
        dynamic_scan_status='SCAN_COMPLETED',
        dynamic_scan_start=date.today(),
        dynamic_scan_end=date.today(),
        api_scan_status='SCAN_COMPLETED',
        api_scan_start=date.today(),
        api_scan_end=date.today(),
        app_hash='hash2',
        modified_app_hash='hashh2',
        score=80,  # Replace with an actual score
        file_path='your_file_path',
    )

    new_scan3 = Scan(
        scan_slug='scan3',
        scan_status='SCAN_COMPLETED',
        scan_created=date.today(),
        scan_start=date.today(),
        scan_end=date.today(),
        static_scan_status='SCAN_COMPLETED',
        static_scan_start=date.today(),
        static_scan_end=date.today(),
        dynamic_scan_status='SCAN_COMPLETED',
        dynamic_scan_start=date.today(),
        dynamic_scan_end=date.today(),
        api_scan_status='SCAN_COMPLETED',
        api_scan_start=date.today(),
        api_scan_end=date.today(),
        app_hash='hash3',
        modified_app_hash='hashh3',
        score=70,  # Replace with an actual score
        file_path='your_file_path',
    )

    new_scan4 = Scan(
        scan_slug='scan4',
        scan_status='SCAN_COMPLETED',
        scan_created=date.today(),
        scan_start=date.today(),
        scan_end=date.today(),
        static_scan_status='SCAN_COMPLETED',
        static_scan_start=date.today(),
        static_scan_end=date.today(),
        dynamic_scan_status='SCAN_COMPLETED',
        dynamic_scan_start=date.today(),
        dynamic_scan_end=date.today(),
        api_scan_status='SCAN_COMPLETED',
        api_scan_start=date.today(),
        api_scan_end=date.today(),
        app_hash='hash4',
        modified_app_hash='hashh4',
        score=60,  # Replace with an actual score
        file_path='your_file_path',
    )


    new_scan5 = Scan(
        scan_slug='scan5',
        scan_status='SCAN_COMPLETED',
        scan_created=date.today(),
        scan_start=date.today(),
        scan_end=date.today(),
        static_scan_status='SCAN_COMPLETED',
        static_scan_start=date.today(),
        static_scan_end=date.today(),
        dynamic_scan_status='SCAN_COMPLETED',
        dynamic_scan_start=date.today(),
        dynamic_scan_end=date.today(),
        api_scan_status='SCAN_COMPLETED',
        api_scan_start=date.today(),
        api_scan_end=date.today(),
        app_hash='hash5',
        modified_app_hash='hashh5',
        score=60,  # Replace with an actual score
        file_path='your_file_path',
    )

    new_scan6 = Scan(
        scan_slug='scan6',
        scan_status='SCAN_COMPLETED',
        scan_created=date.today(),
        scan_start=date.today(),
        scan_end=date.today(),
        static_scan_status='SCAN_COMPLETED',
        static_scan_start=date.today(),
        static_scan_end=date.today(),
        dynamic_scan_status='SCAN_COMPLETED',
        dynamic_scan_start=date.today(),
        dynamic_scan_end=date.today(),
        api_scan_status='SCAN_COMPLETED',
        api_scan_start=date.today(),
        api_scan_end=date.today(),
        app_hash='hash6',
        modified_app_hash='hashh6',
        score=70,  # Replace with an actual score
        file_path='your_file_path',
    )

    new_scan1.save()
    new_scan2.save()
    new_scan3.save()
    new_scan4.save()
    new_scan5.save()
    new_scan6.save()  # Save the new_scan instance to the database



