# accounts/admin.py
from django.contrib import admin
from accounts.models import CustomUser
#admin.site.register(CustomUser)
# accounts/admin.py

class AuthorAdmin(admin.ModelAdmin):
    pass



# Register the CustomUser model with the admin
admin.site.register(CustomUser, AuthorAdmin)
