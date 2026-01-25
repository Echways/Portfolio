from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from info.models import News, Project


class NewsModelTests(TestCase):
    def test_slug_autogeneration_and_uniqueness(self):
        first = News.objects.create(
            title="Slug Test",
            slug="",
            description="desc",
            image="img/news/a.jpg",
        )
        second = News.objects.create(
            title="slug test",
            slug="",
            description="desc",
            image="img/news/b.jpg",
        )
        self.assertEqual(first.slug, "slug-test")
        self.assertEqual(second.slug, "slug-test-2")

    def test_ordering_by_created_at_desc(self):
        base_time = timezone.now()
        older = News.objects.create(
            title="Older",
            slug="",
            description="desc",
            image="img/news/old.jpg",
            created_at=base_time,
        )
        newer = News.objects.create(
            title="Newer",
            slug="",
            description="desc",
            image="img/news/new.jpg",
            created_at=base_time + timedelta(seconds=1),
        )
        ordered = list(News.objects.all())
        self.assertEqual(ordered[0].pk, newer.pk)
        self.assertEqual(ordered[1].pk, older.pk)

    def test_preview_text_truncation(self):
        long_text = "x" * 200
        news = News.objects.create(
            title="Preview",
            slug="",
            description=long_text,
            image="img/news/preview.jpg",
        )
        self.assertTrue(news.preview_text.endswith("..."))
        self.assertEqual(len(news.preview_text), 180)


class ProjectModelTests(TestCase):
    def test_preview_text_passthrough(self):
        project = Project.objects.create(
            title="Short",
            slug="",
            description="short text",
            image="img/projects/short.jpg",
        )
        self.assertEqual(project.preview_text, "short text")
