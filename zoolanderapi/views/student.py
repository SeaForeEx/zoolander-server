from django.http import HttpResponseServerError
from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from zoolanderapi.models import Classroom, User, Student, StudentClass
from rest_framework.decorators import action

class StudentView(ViewSet):

    def retrieve(self, request, pk):
      try:
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
      except Classroom.DoesNotExist as ex: 
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    
    def list(self, request):
      
      students = Student.objects.all()
      serializer = StudentSerializer(students, many=True)
      return Response(serializer.data)
    
    def create(self, request):
        student = Student.objects.create(
            student_full_name = request.data["studentFullName"],
            age = request.data["age"],
            image_url = request.data["imageUrl"],
        )
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def update(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.student_full_name = request.data["studentFullName"]
        student.age = request.data["age"]
        student.image_url = request.data["imageUrl"]
        student.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        
        classroom = Student.objects.get(pk=pk)
        classroom.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    @action(methods=['post'], detail=True)
    def addtoclass(self, request, pk):
        classroom = Classroom.objects.get(pk=request.data["classId"])
        student = Student.objects.get(pk=pk)
        added = StudentClass.objects.create(
            classroom=classroom,
            student=student
        )
        return Response({'message': 'Student added to class'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def remove(self, request, pk):
        classroom = Classroom.objects.get(pk=request.data["classroomId"])
        student = Student.objects.get(pk=pk)
        student_class = StudentClass.objects.get(
            student_id=student.id,
            classroom_id=classroom.id
        )
        student_class.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'student_full_name', 'age', 'image_url')
