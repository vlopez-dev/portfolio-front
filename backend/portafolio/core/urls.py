from django.urls import path,include
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import EnviarCorreo
from .views import download_cv


router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'about', views.AboutViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('send_email/', EnviarCorreo.as_view(), name='send_email'),
    path('download_cv/', download_cv, name='download_cv'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
