from urllib import response
from django.shortcuts import render,get_object_or_404
from .models import Project,About
from rest_framework import viewsets

from .serializers import ProjectSerializer,AboutSerializer

# Create your views here.



class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
    template_name = 'core/index.html'


    def get(self, request, id):
        project = get_object_or_404(Project, pk=id)
        serializer = ProjectSerializer(project)
        print(serializer)
        return response({'serializer': serializer, 'project': project},template_name='index.html')



class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    template_name = 'core/index.html'
    
    
    def get(self, request, id):
        about = get_object_or_404(About, pk=id)
        serializer = AboutSerializer(about)
        print(serializer)
        return response({'serializer': serializer, 'about': about},template_name='index.html')
