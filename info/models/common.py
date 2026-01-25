from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class TimestampedSlugModel(models.Model):
    title = models.CharField("Заголовок", max_length=100, unique=True)
    slug = models.SlugField("Slug", max_length=140, unique=True)
    description = models.TextField()
    image = models.ImageField("Фото")
    created_at = models.DateTimeField("Создано", default=timezone.now)
    updated_at = models.DateTimeField("Обновлено", default=timezone.now)

    class Meta:
        abstract = True
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    @property
    def preview_text(self):
        text = self.description.strip()
        return text if len(text) <= 180 else f"{text[:177]}..."

    def _generate_unique_slug(self) -> str:
        base = slugify(self.title) or self.__class__.__name__.lower()
        candidate = base
        index = 2
        queryset = self.__class__.objects.all()
        while queryset.filter(slug=candidate).exclude(pk=self.pk).exists():
            candidate = f"{base}-{index}"
            index += 1
        return candidate
