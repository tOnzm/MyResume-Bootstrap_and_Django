from django.contrib import admin
from app_general.models import Education, Experience,Skills,Languages,MyProject



# Register your models here.
class EducationAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class ExperienceAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class SkillsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class LanguagesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class MyProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)


