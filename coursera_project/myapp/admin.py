from django.contrib import admin
from .models import Menu
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
# admin.site.unregister(User)
@admin.register(Menu)
class menuAdmin(admin.ModelAdmin):
    list_display=("name","price")
    search_fields=("name__startswith","price")
    

# @admin.register(User)
# class NewAdmin(UserAdmin):
#     readonly_fields = [ 
#         'date_joined', 
#     ] 
#     list_display=("username","email")
#     empty_value_display="-empty-"

#     def get_form(self, request, obj=None, **kwargs): 
#         form = super().get_form(request, obj, **kwargs) 
#         is_superuser = request.user.is_superuser 

#         if not is_superuser: 
#             form.base_fields['username'].disabled = True 

#         return form 



