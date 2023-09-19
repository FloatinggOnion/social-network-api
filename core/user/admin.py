from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.user.models import User, UserManager

# class UserAdmin(BaseUserAdmin):

#     list_display = ["email", "username", "is_superuser"]
#     list_filter = ['is_superuser']
#     fieldsets = [
#         (None, {"fields": ["email", "password"]}),
#         ("Personal info", {"fields": ["username"]}),
#         ("Permissions", {"fields": ["is_superuser"]}),
#     ]

#     add_fieldsets = [
#         (
#             None,
#             {
#                 "classes": ["wide"],
#                 "fields": ["email", "username", "password1", "password2"],
#             },
#         ),
#     ]
#     search_fields = ["email"]
#     ordering = ["email"]
#     filter_horizontal = []