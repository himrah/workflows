from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Department)
admin.site.register(Inbox)
admin.site.register(Sent_item)
admin.site.register(Trash)