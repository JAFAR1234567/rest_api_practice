from rest_framework import serializers
from .models import Course

class Course_serializer(serializers.ModelSerializer):
    
	class Meta:
          model = Course
          fields = ['id','teacher_name','course_name','course_duration','seat',]
  

  