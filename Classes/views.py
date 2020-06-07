from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ClassContent
from .serializers import ClassSerializer


# Create your views here.
@api_view(['GET', "POST"])
def api_function(request):
    if request.method == 'GET':
        classes_list = ClassContent.objects.filter()
        classes_serializer = ClassSerializer(classes_list, many=True)
        return Response(classes_serializer.data)
    elif request.method == 'POST':
        classes_serializer = ClassSerializer(data=request.data)
        if classes_serializer.is_valid():
            classes_serializer.save()
            return Response(classes_serializer.data, status=status.HTTP_201_CREATED)
    return Response(classes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)