from django.db import models
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attached_file = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return f"Request {self.id} by {self.customer.name}"
