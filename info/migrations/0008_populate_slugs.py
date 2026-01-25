from django.db import migrations
from django.utils.text import slugify


def _generate_unique_slug(model, title: str, pk: int) -> str:
    base = slugify(title) or "item"
    candidate = base
    index = 2
    while model.objects.filter(slug=candidate).exclude(pk=pk).exists():
        candidate = f"{base}-{index}"
        index += 1
    return candidate


def populate_slugs(apps, schema_editor):
    News = apps.get_model("info", "News")
    Project = apps.get_model("info", "Project")

    for obj in News.objects.all():
        obj.slug = _generate_unique_slug(News, obj.title, obj.pk)
        obj.save(update_fields=["slug"])

    for obj in Project.objects.all():
        obj.slug = _generate_unique_slug(Project, obj.title, obj.pk)
        obj.save(update_fields=["slug"])


def noop(apps, schema_editor):
    return None


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0007_add_slugs"),
    ]

    operations = [
        migrations.RunPython(populate_slugs, reverse_code=noop),
    ]

