from django.contrib import admin

from .models import *

admin.site.register(Grade)
admin.site.register(Section)
admin.site.register(SectionSubject)
admin.site.register(SectionAttendance)
