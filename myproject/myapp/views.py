from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")


class ItemCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            total_count = Item.objects.count()
            return Response({
                'message': 'Item created successfully',
                'data': serializer.data,
                'total_count': total_count,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
