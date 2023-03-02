from urllib import response
from mailjet_rest import Client

from django.shortcuts import render,get_object_or_404
from .models import Project,About
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.http import FileResponse

from .serializers import ProjectSerializer,AboutSerializer
from django.conf import settings

from captcha.decorators import validate_recaptcha



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





class EnviarCorreo(APIView):

    # def post(self, request, *args, **kwargs):
    #      message = request.data.get('message')
    #      from_email = request.data.get('email')
    #      recipient_list = ['victorl_222@hotmail.com']
    #      send_mail('Subject', 'Message', 'victorl_222@hotmail.com', ['valopezr5@gmail.com'])
    #      return Response({'message': 'Email sent successfully'})


    @validate_recaptcha
    def post(self, request, *args, **kwargs):
        message = request.data.get('message')
        from_email = request.data.get('email')
        recipient_list = ['victorl_222@hotmail.com']
        captcha = ReCaptchaField()
        print("Tengo los datos")

        mailjet = Client(auth=(settings.MJ_APIKEY_PUBLIC, settings.MJ_APIKEY_PRIVATE), version='v3.1')
        data = {
            'Messages': [
                {
                    'From': {
                        'Email': settings.DEFAULT_FROM_EMAIL
                    },
                    'To': [
                        {
                            'Email': settings.MJ_TO_EMAIL,
                            'Name': settings.MJ_TO_NAME
                        }
                    ],
                    'Subject': 'Mensaje de contacto desde tu sitio web',
                    'TextPart': message,
                    'ReplyTo': {
                        'Email': from_email
                    }
                }
            ]
        }
        result = mailjet.send.create(data=data)

        if result.status_code == 200:
            return Response({'message': 'Email sent successfully'})
        else:
            return Response({'message': 'Error sending email'}, status=status.HTTP_400_BAD_REQUEST)





def download_cv(request):
    file = open('media/cv.pdf', 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    return response