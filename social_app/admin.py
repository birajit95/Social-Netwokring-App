from django.contrib import admin

# Register your models here.
from .models import User, FriendStatus

admin.site.register(User)
admin.site.register(FriendStatus)
