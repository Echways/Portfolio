from django.db import models

from info.models.common import TimestampedSlugModel


class Project(TimestampedSlugModel):
    description = models.TextField("Описание проекта")
    image = models.ImageField("Фото", upload_to="img/projects")

    class Meta(TimestampedSlugModel.Meta):
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
