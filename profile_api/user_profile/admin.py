from django.contrib import admin
# from .models import UserProfile

from user_profile import models


admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)