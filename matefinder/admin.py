from django.contrib import admin

from .models import Student, RequestInformation, SentRequestInformation, DormInformation

admin.site.register(Student)
admin.site.register(RequestInformation)
admin.site.register(SentRequestInformation)
admin.site.register(DormInformation)
