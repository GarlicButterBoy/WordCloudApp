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

@        