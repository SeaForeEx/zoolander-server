# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from zoolanderapi.models import User, Classroom, Assignment

class AssignmentView(ViewSet):
    """CRUD Assignments"""
    
    def create(self, request):
        """POST Assignment"""
        teacher_id = User.objects.get(uid=request.data["teacherId"])
        class_id = Classroom.objects.get(pk=request.data["classId"])
        assignment = Assignment.objects.create(
            teacher_id = teacher_id,
            class_id = class_id,
            content=request.data["content"],
            title=request.data["title"],
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
        
        assignments = Assignment.objects.all()
        class_id = request.query_params.get('classId', None)
        if class_id is not None:
            assignments = assignments.filter(class_id=class_id)
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def update(self, request, pk):
        """PUT Assignment"""
        
        assignment = Assignment.objects.get(pk=pk)
        class_id = Classroom.objects.get(pk=request.data["classId"])
        assignment.class_id=class_id
        assignment.content = request.data["content"]
        assignment.title = request.data["title"]
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
        fields = ('id', 'teacher_id', 'class_id', 'content', 'title')
        depth = 1
