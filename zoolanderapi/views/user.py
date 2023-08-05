from django.http import HttpResponseServerError
from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from zoolanderapi.models import User

class UserView(ViewSet):
  
  def retrieve(self,request,pk):
    try:
      user = User.objects.get(pk=pk)
      serializer = UserSerializer(user)
      return Response(serializer.data)
    except User.DoesNotExist as ex:
      return Response({'message': ex.args[0]},
                      status=status.HTTP_404_NOT_FOUND)
      
  def list(self, request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
class UserSerializer(serializers.ModelSerializer):
  class Meta: 
    model = User
    fields = ('id', 'uid')
