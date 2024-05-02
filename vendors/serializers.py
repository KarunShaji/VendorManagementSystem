from rest_framework import serializers
from .models import Vendor
from django.contrib.auth.models import User

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_details', 'address', 'vendor_code', 
                  'on_time_delivery_rate', 'quality_rating_avg', 
                  'average_response_time', 'fulfillment_rate']


