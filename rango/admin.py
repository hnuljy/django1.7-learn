from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
#Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', 'views')}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(UserProfile)

# Register your models here.
