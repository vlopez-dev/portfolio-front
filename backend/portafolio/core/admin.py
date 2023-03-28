from django.contrib import admin
from .models import Project,About,Contact,Certificate

# Register your models here.
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Certificate)
