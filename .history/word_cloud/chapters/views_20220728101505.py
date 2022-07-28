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

        serializer = ChapterSerializer
