# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from zoolanderapi.models import User, Classroom, Assignment

class AssignmentView(ViewSet):
    """CRUD Assignments"""
    
    def create(self, request):
        """POST Assignment"""
        teacher_id = User.objects.get(pk=request.data["teacherId"])
        class_id = Classroom.objects.get(pk=request.data["classId"])
        assignment = Assignment.objects.create(
            teacher_id = teacher_id,
            class_id = class_id,
            content=request.data["content"],
        )
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def retrieve(self, request, pk):
        """GET Single Assignment"""
        
        assignment = Assignment.objects.get(pk=pk)
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def list(self, request):
        """GET All Assignments"""
        
        assignment = Assignment.objects.all()
        serializer = AssignmentSerializer(assignment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def update(self, request, pk):
        """PUT Assignment"""
        
        assignment = Assignment.objects.get(pk=pk)
        assignment.content = request.data["content"]
        assignment.save()
        return Response('Assignment Updated', status=status.HTTP_200_OK)
      
    def destroy(self, request, pk):
        """DELETE Assignment"""
        
        assignment = Assignment.objects.get(pk=pk)
        assignment.delete()
        return Response('Assignment Deleted', status=status.HTTP_204_NO_CONTENT)
      
class AssignmentSerializer(serializers.ModelSerializer):
    """JSON Serializer for Assignments"""
    
    class Meta:
        model = Assignment
        fields = ('id', 'teacher_id', 'class_id', 'content')
    
