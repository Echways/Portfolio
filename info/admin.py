from django.contrib import admin

from .models import Achievement, News, Project, TeamMember


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "updated_at")
    search_fields = ("title", "slug", "description")
    ordering = ("-created_at",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "updated_at")
    search_fields = ("title", "slug", "description")
    ordering = ("-created_at",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("id", "short_text")
    search_fields = ("text",)
    ordering = ("id",)

    def short_text(self, obj):
        return obj.text[:80]

    short_text.short_description = "Текст"


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name", "skills")
    ordering = ("order", "name")
