from django.db import models


class Enquiry(models.Model):

    CATEGORY_CHOICES = [
        ('website', 'Website Development'),
        ('mobile', 'Mobile Application Development'),
        ('ai', 'AI Software Development'),
        ('marketing', 'Digital Marketing'),
        ('ecommerce', 'E-commerce Development'),
        ('custom', 'Custom Software Development'),
        ('other', 'Other Services'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('converted', 'Converted'),
    ]

    # Customer Information
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    # AI Analysis Information
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other'
    )

    budget = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )

    requirements = models.JSONField(default=list, blank=True)
    missing_information = models.TextField(blank=True)
    ai_summary = models.TextField(blank=True)
    suggested_response = models.TextField(blank=True)

    # Enquiry Management
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name
