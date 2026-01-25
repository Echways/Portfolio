from django.db import models


class TeamMember(models.Model):
    name = models.CharField("Имя", max_length=100)
    skills = models.CharField("Навыки", max_length=200, blank=True)
    telegram_url = models.URLField("Telegram", blank=True)
    instagram_url = models.URLField("Instagram", blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Участник команды"
        verbose_name_plural = "Команда"
        ordering = ("order", "name")

    def __str__(self):
        return self.name
