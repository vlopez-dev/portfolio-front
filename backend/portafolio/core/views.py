from http.client import HTTPResponse
from telnetlib import STATUS
from urllib import response
from mailjet_rest import Client
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from .models import Project,About
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse

from .serializers import ProjectSerializer,AboutSerializer
from django.conf import settings
import requests
import json
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from captcha.fields import CaptchaField
public_key = settings.RECAPTCHA_PUBLIC_KEY
secret_key = settings.RECAPTCHA_PRIVATE_KEY


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
    
    
    def post(self, request, *args, **kwargs):
        message = request.data.get('message')
        reply_to = request.data.get('email')
        sender_email = 'web@vic.uy'
        recipient_list = ['web@vic.uy']

        # Verificar ReCAPTCHA
        captcha_response = request.data.get('g-recaptcha-response')
        success = captcha_contact(captcha_response, request.META.get('REMOTE_ADDR'))
        if not success:
            return Response({'message': 'Invalid reCAPTCHA'}, status=STATUS.HTTP_400_BAD_REQUEST)
        else:

            email = EmailMessage(
                subject='Correo desde Web',
                body=message,
                from_email=sender_email,
                to=recipient_list,
                reply_to=[reply_to],
                headers={'Reply-To': reply_to}
            )
            email.send()
            return Response({'message': 'Correo enviado exitosamente'})



def download_cv(request):
    file = open('media/cv.pdf', 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    return response




def captcha_contact(captcha_response,remote_ip):
      # Obtener la respuesta del captcha del formulario
   
    # Realizar la verificación del captcha con Google
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    params = {
        'secret': secret_key,
        'response': captcha_response,
        'remoteip': remote_ip
    }
    response = requests.post(verify_url, data=params)
    response_json = json.loads(response.text)

    return response_json.get('success', False)
