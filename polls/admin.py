from django.contrib import admin
from polls.models import Question, Choice, EyewitnessStimuli, Users, Response


# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(EyewitnessStimuli)
admin.site.register(Users)
admin.site.register(Response)
