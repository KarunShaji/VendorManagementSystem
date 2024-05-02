from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from vendors.models import Vendor
from django.utils import timezone

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number



@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_metrics(sender, instance, created, **kwargs):
    if created or instance.status == 'completed':
        vendor = instance.vendor
        
        # Update On-Time Delivery Rate
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        on_time_orders = completed_orders.filter(delivery_date__lte=timezone.now())
        on_time_delivery_rate = on_time_orders.count() / completed_orders.count() if completed_orders.count() > 0 else 0
        vendor.on_time_delivery_rate = on_time_delivery_rate
        
        # Update Quality Rating Average
        completed_orders_with_rating = completed_orders.exclude(quality_rating=None)
        quality_rating_avg = completed_orders_with_rating.aggregate(avg_rating=models.Avg('quality_rating'))['avg_rating']
        vendor.quality_rating_avg = quality_rating_avg if quality_rating_avg else 0
        
        # Update Average Response Time
        completed_orders_with_acknowledgment = completed_orders.exclude(acknowledgment_date=None)
        response_times = [(order.acknowledgment_date - order.issue_date).total_seconds() for order in completed_orders_with_acknowledgment]
        average_response_time = sum(response_times) / len(response_times) if response_times else 0
        vendor.average_response_time = average_response_time
        
        # Update Fulfillment Rate
        fulfilled_orders = completed_orders.exclude(acknowledgment_date=None).exclude(quality_rating=None)
        fulfillment_rate = fulfilled_orders.count() / completed_orders.count() if completed_orders.count() > 0 else 0
        vendor.fulfillment_rate = fulfillment_rate
        
        vendor.save()