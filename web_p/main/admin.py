from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(InviteProj)
admin.site.register(MembershipProject)

