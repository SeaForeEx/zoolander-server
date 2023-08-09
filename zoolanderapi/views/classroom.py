from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from zoolanderapi.models import Classroom, User, StudentClass
from rest_framework.decorators import action

class ClassroomView(ViewSet):

    def retrieve(self, request, pk):
        """Docstring"""
        try:
            classroom = Classroom.objects.get(pk=pk)
            serializer = ClassroomSerializer(classroom)
            return Response(serializer.data)
        except Classroom.DoesNotExist as ex: 
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    
    def list(self, request):
        """Docstring"""
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Docstring"""
        teacher_id = User.objects.get(uid=request.data["teacherId"])
        classroom = Classroom.objects.create(
            teacher_id=teacher_id,
            class_name = request.data["className"],
            description = request.data["description"],
        )
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Docstring"""
        classroom = Classroom.objects.get(pk=pk)
        teacher_id = User.objects.get(uid=request.data["teacherId"])
        classroom.teacher_id=teacher_id
        classroom.class_name = request.data["className"]
        classroom.description = request.data["description"]
        classroom.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        
        classroom = Classroom.objects.get(pk=pk)
        classroom.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    @action(methods=['get'], detail=True)
    def get_students(self, request, pk):
      try:
        student_classes = StudentClass.objects.filter(classroom_id = pk)
        serializer = StudentClassSerializer(student_classes, many=True)
        return Response(serializer.data)
      except StudentClass.DoesNotExist:
        return Response(False)

class StudentClassSerializer(serializers.ModelSerializer):
  class Meta: 
    model = StudentClass
    fields = ('id', 'classroom', 'student')
    depth = 1

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('id', 'class_name', 'teacher_id', 'description')
        depth = 1
