from django.contrib import admin

from accounts.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin configutation of User model.
    """
    list_display = ("user_name", "email", "date_joined")
    list_filter = ("email",)
    readonly_fields = ("email",)
    search_fields = ("email",)
    ordering = ("date_joined",)
    fieldsets = (
        ("User", {
            "fields": ("email", "password", "username")
        }),
        ("Personal info", {
            "fields": ("first_name", "last_name")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Important dates", {
            "fields": ("last_login", "date_joined")
        }),
    )

    def user_name(self, obj):
        name = ("" + getattr(obj, "first_name") + " " + getattr(obj, "last_name")).strip()
        return name if name else "No name"
