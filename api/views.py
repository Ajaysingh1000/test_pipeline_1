from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import BookSerializer
from .models import Book


class BookAPIView(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if not serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
