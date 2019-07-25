from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display=("your_name","email","password")
	search_fields=("your_name","email")

admin.site.register(User,UserAdmin)


	
	

