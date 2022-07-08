from django.contrib import admin

from lamiapp.models import  event_pic, main_page_pic, potraits, projects
from lamiapp.views import potrait

# Register your models here.
admin.site.register(main_page_pic)
admin.site.register(potraits)
admin.site.register(event_pic)
admin.site.register(projects)


# 
