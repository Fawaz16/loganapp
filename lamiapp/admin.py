from django.contrib import admin

from lamiapp.models import  booking, droneshot, event_pic, main_page_pic, potrait_pic, project


# Register your models here.
admin.site.register(main_page_pic)
admin.site.register(potrait_pic)
admin.site.register(event_pic)
admin.site.register(project)
admin.site.register(booking)
admin.site.register(droneshot)



# 
