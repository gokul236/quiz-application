from django.contrib import admin
from .models import login
from .models import register
from .models import questionstable
admin.site.register(login)
admin.site.register(register)
admin.site.register(questionstable)
