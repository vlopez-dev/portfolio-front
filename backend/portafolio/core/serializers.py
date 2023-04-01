from django.conf import settings
from .models import Project,About,Contact,Certificate,Technology

from rest_framework import serializers



class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('name','icon')





class ProjectSerializer(serializers.ModelSerializer):
    technologys = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'pro_img', 'link_repo','link_live','technologys')

    def get_technologys(self, obj):
        technology_ids = obj.technologys.values_list('id', flat=True)
        technologies = Technology.objects.filter(id__in=technology_ids)
        return [{'id': t.id, 'name': t.name,'icon':t.icon} for t in technologies]




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