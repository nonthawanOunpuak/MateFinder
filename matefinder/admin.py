from django.contrib import admin

from .models import Student, RequestInformation, SentRequestInformation, DormInformation, CheckLists

admin.site.register(Student)
admin.site.register(RequestInformation)
admin.site.register(SentRequestInformation)
admin.site.register(DormInformation)
admin.site.register(CheckLists)