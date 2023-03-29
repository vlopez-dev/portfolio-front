from .models import Project,About,Contact,Certificate,Technology

from rest_framework import serializers



class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('name','icon')

class ProjectSerializer(serializers.ModelSerializer):
    
    technologys=TechnologySerializer(many=True,read_only=True)

    class Meta:
        model = Project
        fields = ('id','name','description','pro_img','link_repo','link_live','technologys')







class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title','description','imagenabout')
        
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('title','description')
        
        

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('title','imagecert')