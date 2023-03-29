from .models import Project,About,Contact,Certificate

from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'




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