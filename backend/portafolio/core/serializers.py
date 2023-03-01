from .models import Project,About

from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name','description','pro_img','link_repo','link_live')
        
        
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title','description','imagenabout','bio')