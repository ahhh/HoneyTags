from django.contrib import admin

from .models import Tag
from .models import Callbacks

admin.site.register(Tag)
admin.site.register(Callbacks)
