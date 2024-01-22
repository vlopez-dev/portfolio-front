from http.client import HTTPResponse
from telnetlib import STATUS
from urllib import response
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from .models import Project,About,Contact,Certificate,Technology
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.generics import ListAPIView
from .serializers import ProjectSerializer,AboutSerializer,ContactSerializer,CertificateSerializer
from django.conf import settings
import requests
import json
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse
from rest_framework import status
from captcha.fields import CaptchaField
import logging
from django.core.files.storage import default_storage

logger = logging.getLogger('portafolio')

public_key = settings.RECAPTCHA_PUBLIC_KEY
secret_key = settings.RECAPTCHA_PRIVATE_KEY


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
    template_name = 'core/index.html'


    def get(self, request, id):
        project = get_object_or_404(Project, pk=id)
        serializer = ProjectSerializer(project)
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



class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    template_name = 'core/index.html'
    
    
    def get(self, request, id):
        contact = get_object_or_404(Contact, pk=id)
        serializer = ContactSerializer(contact)
        print(serializer)
        return response({'serializer': serializer, 'contact': contact},template_name='index.html')




class CertificateViewSet(viewsets.ModelViewSet):

    queryset = Certificate.objects.all().order_by('id')
    serializer_class = CertificateSerializer
    template_name = 'core/index.html'


    def get(self, request, id):
        certificate = get_object_or_404(Certificate, pk=id)
        serializer = CertificateSerializer(certificate)
        print(serializer)
        return response({'serializer': serializer, 'certificate': certificate},template_name='index.html')







class EnviarCorreo(APIView):
    
    
    def post(self, request, *args, **kwargs):
        csrf_cookie_value = request.COOKIES.get('csrftoken')
        message = request.data.get('message')
        reply_to = request.data.get('email')
        sender_email = 'web@vic.uy'
        recipient_list = ['web@vic.uy']

        # Verificar ReCAPTCHA
        captcha_response = request.data.get('recaptchaResponse')
        success = captcha_contact(captcha_response, request.META.get('REMOTE_ADDR'))
        logger = logging.getLogger('portafolio')
        logger.debug(f'The value of success is {success}')
        if success:

            email = EmailMessage(
                subject='Correo desde Web',
                body=message,
                from_email=sender_email,
                to=recipient_list,
                reply_to=[reply_to],
                headers={'Reply-To': reply_to}
            )
            try:
                email.send()

                return JsonResponse({'message': 'Correo enviado exitosamente'})
            except:
              return JsonResponse({'message': 'Correo no enviado'}, status=400)
            
        else:
            return JsonResponse({'message': 'Invalid reCAPTCHA'}, status=400)







def download_cv(request):
    file = open('media/media/cv.pdf', 'rb')
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
        'remoteip': remote_ip,
    }
    response = requests.post(verify_url, data=params)
    response_json = json.loads(response.text)
    logger = logging.getLogger('portafolio')
    logger.debug(f'The value of secret_key is {secret_key}, remoteip{remote_ip}')

    return response_json.get('success', False)
