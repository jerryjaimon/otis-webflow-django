from django.urls import get_resolver
from django.shortcuts import render,redirect
from main_app.models import Application,Scan  # Import the Application model
from datetime import date  # Import the date module
from django.http import HttpResponse
import hashlib
import os


def index_page(request):
    applications = Application.objects.all()
    return render(request, 'detail_client.html', {'applications': applications})

def asset_page(request,slug):
    try:
        application = Application.objects.get(app_slug=slug)
        app_hash = application.app_hash
        scans = Scan.objects.filter(app_hash=app_hash)
        asset_name = application.app_name
        context = {'scans': scans,'asset_name':asset_name}
    except Application.DoesNotExist:
        # Handle the case where the application with the given slug does not exist
        return None
    return render(request, 'detail_asset.html',context)

def report_page(request):
    return render(request, 'detail_reports.html')

def login_page(request):
    return render(request, 'log-in.html')

def submit_application(request):
    if request.method == 'POST':
        # Retrieve form 
        print(request.POST)
        uploaded_file = request.FILES['fileToUpload']
        
        try:
            # Calculate the MD5 hash of the uploaded file
            md5_hash = hashlib.md5()
            for chunk in uploaded_file.chunks():
                md5_hash.update(chunk)
            
            md5_digest = md5_hash.hexdigest()

            # Perform any additional actions with the MD5 hash, such as saving it to the database
            # Example: application = Application(app_name='YourAppName', file=uploaded_file, md5=md5_digest)
            # application.save()

        except Exception as e:
           print(e)

        new_filename = f"{md5_digest}.apk"  # You can specify the file extension you expect

        # Save the file to a desired location with the new filename
        file_path = os.path.join(new_filename)
        with open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        asset_name = request.POST.get('Contact-4-Last-Name')
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        domain = request.POST.get('Asset-ID')
        upload_date = date.today()
        ssl_pinned = 'True'
        root_detection = 'True'
        file_status = "WEBFLOW_UPLOADED"
        app_hash = md5_digest

        # Create a new Application instance and save it
        new_application = Application(
            app_hash = app_hash,
            app_name=asset_name,
            username=username,
            password=password,
            domain=domain,
            upload_date = upload_date,
            ssl_pinned = ssl_pinned,
            root_detection = root_detection,
            file_status = file_status,
            app_slug= md5_digest,
            type="Android"

        )
        print(new_application.save())
        return redirect('index_page')  # Redirect to a success page or the desired URL

    return HttpResponse("Invalid request method")

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



