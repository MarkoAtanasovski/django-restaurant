from django.contrib import admin

# Register your models here.
from Base_App.models import *


admin.site.register(ItemList)
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(Feedback)
admin.site.register(BookTable)

