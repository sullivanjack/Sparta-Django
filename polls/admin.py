from django.contrib import admin

from .models import Question, Player, Round, Course

# Register your models here.
admin.site.register(Question)
admin.site.register(Player)
admin.site.register(Round)
admin.site.register(Course)
