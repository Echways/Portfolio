from django.db import models


class Achievement(models.Model):
    text = models.TextField("Достижение")

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        ordering = ("id",)

    def __str__(self):
        return self.text[:80]
