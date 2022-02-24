from django.contrib import admin

# Register your models here.
from .models import *

admin.site.site_header = 'VR'
admin.site.register(home)
admin.site.register(Challenges)
admin.site.register(about_us)
admin.site.register(contact)
admin.site.register(training)
admin.site.register(our_goal)