from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm
from django import forms
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Vendor
from .serializers import VendorSerializer


# Register a User

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    form = ExtendedUserCreationForm(request.data)
    if form.is_valid():
        form.save()
        return Response("Account created successfully", status=status.HTTP_201_CREATED)
    else:
        print(form.errors)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


# Login a User

@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'id': user.id, 'username': user.username, 'token': token.key}, status=status.HTTP_200_OK)


# User Logout

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'Message': 'You are logged out'},status=status.HTTP_200_OK)

# Add or List Vendor

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def vendors(request, vendor_id=None):
    if request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({'id': instance.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if vendor_id is not None:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
                serializer = VendorSerializer(vendor)
                return Response(serializer.data)
            except Vendor.DoesNotExist:
                return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            vendors = Vendor.objects.all()
            serializer = VendorSerializer(vendors, many=True)
            return Response(serializer.data)


# List or Update or Delete Single Vendor

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def retrieve_update_delete_vendor(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vendor.delete()
        return Response({'message': 'Vendor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)