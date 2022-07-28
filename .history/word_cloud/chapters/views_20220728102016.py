from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Chapter
from .serializers import *

# Create your views here.
@api_view(['GET','POST'])
def chapters_list(request):
    if request.method == 'GET':
        data = Chapter.objects.all()
        serializer = ChapterSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChapterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def chapters_detail(request, pk):
    try:
        chapter = Chapter.objects.all()
    except Chapter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='PUT':
        serializer = ChapterSerializer(chapter, data=request.data, context={'request': request})    
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.)                