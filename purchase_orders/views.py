from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from vendors.models import Vendor
from django.shortcuts import get_object_or_404

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def create_list_purchase_orders(request):
    if request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        vendor_id = request.query_params.get('vendor')
        if vendor_id:
            try:
                vendor_id = int(vendor_id)
            except ValueError:
                return Response({'error': 'Invalid vendor ID'}, status=status.HTTP_400_BAD_REQUEST)
            # Check if the vendor exists
            if not Vendor.objects.filter(id=vendor_id).exists():
                return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
            purchase_orders = PurchaseOrder.objects.filter(vendor=vendor_id)
        else:
            purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def retrieve_update_delete_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        purchase_order.delete()
        return Response({'message': 'Purchase order deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vendor_performance(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    performance_metrics = {
        'on_time_delivery_rate': vendor.on_time_delivery_rate,
        'quality_rating_avg': vendor.quality_rating_avg,
        'average_response_time': vendor.average_response_time,
        'fulfillment_rate': vendor.fulfillment_rate
    }
    return Response(performance_metrics)