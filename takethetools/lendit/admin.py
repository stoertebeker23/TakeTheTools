from django.contrib import admin
from .models import (
    Tool,
    Purpose,
    Lendlog,
    Category,
    CustomUser,
    CustomImage
)
# Register your models here.


admin.site.register(Tool)
admin.site.register(Purpose)
admin.site.register(Lendlog)
admin.site.register(Category)
admin.site.register(CustomUser)
admin.site.register(CustomImage)

