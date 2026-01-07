from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age", "created_at")
    search_fields = ("first_name", "last_name")
    list_filter = ("age",)