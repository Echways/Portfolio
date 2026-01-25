from django.db import models

from info.models.common import TimestampedSlugModel


class News(TimestampedSlugModel):
    description = models.TextField("Текст новости")
    image = models.ImageField("Фото", upload_to="img/news")

    class Meta(TimestampedSlugModel.Meta):
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
