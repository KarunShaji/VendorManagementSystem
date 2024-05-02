from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer

@api_view(['GET'])
@permission_classes([])
def vendor_performance(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Calculate performance metrics
    on_time_delivery_rate = vendor.on_time_delivery_rate
    quality_rating = vendor.quality_rating_avg
    response_time = vendor.average_response_time
    fulfillment_rate = vendor.fulfillment_rate
    
    # Prepare response data
    performance_data = {
        'on_time_delivery_rate': on_time_delivery_rate,
        'quality_rating': quality_rating,
        'response_time': response_time,
        'fulfillment_rate': fulfillment_rate
    }
    
    return Response(performance_data, status=status.HTTP_200_OK)
