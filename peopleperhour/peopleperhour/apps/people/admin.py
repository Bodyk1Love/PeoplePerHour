from django.contrib import admin

from .models import User, Worker

admin.site.register(User)
admin.site.register(Worker)
