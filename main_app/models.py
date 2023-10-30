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

class Scan(models.Model):
    SCAN_STATUS_CHOICES = [
        ('IN_QUEUE', 'In Queue'),
        ('SCAN_INITIATED', 'Scan Initiated'),
        ('SCAN_COMPLETED', 'Scan Completed'),
        ('FAILED', 'Failed'),
    ]
    
    scan_slug = models.CharField(max_length=255, primary_key=True)

    scan_status = models.CharField(max_length=20, choices=SCAN_STATUS_CHOICES)
    scan_created = models.DateField(default=None, null=True, blank=True)
    scan_start = models.DateField(default=None, null=True, blank=True)
    scan_end = models.DateField(default=None, null=True, blank=True)


    static_scan_status = models.CharField(max_length=20, choices=SCAN_STATUS_CHOICES)
    static_scan_start = models.DateField(default=None, null=True, blank=True)
    static_scan_end = models.DateField(default=None, null=True, blank=True)

    dynamic_scan_status = models.CharField(max_length=20, choices=SCAN_STATUS_CHOICES)
    dynamic_scan_start = models.DateField(default=None, null=True, blank=True)
    dynamic_scan_end = models.DateField(default=None, null=True, blank=True)

    api_scan_status = models.CharField(max_length=20, choices=SCAN_STATUS_CHOICES)
    api_scan_start = models.DateField(default=None, null=True, blank=True)
    api_scan_end = models.DateField(default=None, null=True, blank=True)

    app_hash = models.CharField(max_length=255)
    modified_app_hash = models.CharField(max_length=255)
    score = models.IntegerField(default=None, null=True, blank=True)    
    file_path = models.CharField(max_length=255)

    class Meta:
        db_table = 'scan'

    def __str__(self):
        return f"Scan {self.scan_id} - {self.scan_status}"


class Report(models.Model):
    report_id = models.CharField(max_length=255, primary_key=True)
    scan_id = models.ForeignKey(Scan, on_delete=models.CASCADE)
    
    REPORT_STATUS_CHOICES = [
        ('IN_PROCESS', 'In Process'),
        ('GENERATED', 'Generated'),
        ('FAILED', 'Failed'),
    ]
    report_status = models.CharField(max_length=20, choices=REPORT_STATUS_CHOICES)
    
    score = models.IntegerField()
    high_vulnerability_count = models.IntegerField()
    medium_vulnerability_count = models.IntegerField()
    low_vulnerability_count = models.IntegerField()
    info_vulnerability_count = models.IntegerField()
    
    test_case_executed_count = models.IntegerField()
    test_case_dropped_count = models.IntegerField()
    test_case_inconclusive_count = models.IntegerField()
    
    m1_issues_count = models.IntegerField()
    m2_issues_count = models.IntegerField()
    m3_issues_count = models.IntegerField()
    m4_issues_count = models.IntegerField()
    m5_issues_count = models.IntegerField()
    m6_issues_count = models.IntegerField()
    m7_issues_count = models.IntegerField()
    m8_issues_count = models.IntegerField()
    m9_issues_count = models.IntegerField()
    m10_issues_count = models.IntegerField()
    
    report_path = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'report'

    def __str__(self):
        return f"Report {self.report_id} - {self.report_status}"
    
