from django.contrib import admin
from .models import MenuItem, PhotoAvatar, UserProfile


class PhotoAvatarAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(MenuItem)
admin.site.register(PhotoAvatar)
admin.site.register(UserProfile)
