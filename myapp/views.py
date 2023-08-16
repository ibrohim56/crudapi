from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializers
from .models import Student
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
@api_view(['GET', 'POST'])
def test_get(request):
    std = Student.objects.all()
    serializers = StudentSerializers(std, many=True)

    return Response({'status': 200, 'data': serializers.data})


@api_view(['GET', 'POST'])
def test_post(request):
    serializer = StudentSerializers(data=request.data)
    if not serializer.is_valid():
        return Response({'status': 403, 'message': 'xatolik yuz berdi'})
    serializer.save()

    return Response({'status': 200, 'data': serializer.data, 'message': 'Malumot olindi'})


@api_view(['PUT', 'GET'])
def test_put(request, id):
    std = Student.objects.get(id=id)
    try:
        serializer = StudentSerializers(std, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'status': 403, 'message': 'xatolik yuz berdi'})
        serializer.save()
        return Response({'status': 200, 'data': serializer.data, 'message': 'Malumot yangilandi'})
    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'Xato id!'})


@api_view(['DELETE', 'GET'])
def test_delete(request, id):
    std = Student.objects.get(id=id)
    std.delete()
    return Response({'status': 200, 'message': 'Ochirildi'})
