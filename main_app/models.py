from django.db import models

class Application(models.Model):
    app_slug = models.CharField(max_length=255, primary_key=True)
    app_hash = models.CharField(max_length=255,default=None)
    app_name = models.CharField(max_length=255,default=None)
    type = models.CharField(max_length=10)  # You can specify choices if needed (e.g., choices=[('ANDROID', 'Android'), ('IOS', 'iOS')])

    SSL_PINNED_CHOICES = [
        ('TRUE', 'TRUE'),
        ('FALSE', 'FALSE'),
    ]
    
    ROOT_DETECTION_CHOICES = [
        ('TRUE', 'TRUE'),
        ('FALSE', 'FALSE'),
    ]
    
    file_status = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    upload_date = models.DateField(blank=True, null=True)
    
    ssl_pinned = models.CharField(max_length=10, choices=SSL_PINNED_CHOICES, default='TRUE')
    root_detection = models.CharField(max_length=10, choices=ROOT_DETECTION_CHOICES, default='TRUE')

    def __str__(self):
        return f"Scan Result - {self.file_status}"
