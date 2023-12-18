from django.contrib import admin
from portfolio.models import Skill, Project, Education, Experience, Recommendation


class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "icon")
    list_display_links = ("title",)
    list_editable = ("description", "icon")
    search_fields = ("title",)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "url")
    list_display_links = ("title",)
    list_editable = ("description", "url")
    search_fields = ("title",)


class EducationAdmin(admin.ModelAdmin):
    list_display = ("title", "start_end_date", "description", "url")
    list_display_links = ("title",)
    list_editable = ("start_end_date", "description", "url")
    search_fields = ("title",)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("company", "role", "start_end_date")
    list_display_links = ("role",)
    list_editable = ("company", "start_end_date")
    search_fields = ("company",)


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "company", "description")
    list_display_links = ("name",)
    list_editable = ("role", "company", "description")
    search_fields = ("name",)


admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
