from django.shortcuts import render
from rest_framework.views import APIView
from .models import Item
from django.http import Http404
from .Serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class GetItem(APIView):
    def get_item(self, pk):
        try:
            return Item.objects.get(id=pk)
        except Item.DoesNotExist:
            return Http404

    def get(self, request, pk):
        item = self.get_item(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_item(pk)
        if request.method == 'PUT':
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error, status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, pk):
        item = self.get_item(pk)
        if request.method == 'DELETE':
            item.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


class ListItem(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'description']
    pagination_class = PageNumberPagination
