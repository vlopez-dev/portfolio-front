from django.contrib import admin
from .models import Project,About,Contact,Certificate,Technology,Personalcv

# Register your models here.
admin.site.register(Project)
admin.site.register(Technology)

admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Certificate)
admin.site.register(Personalcv)
