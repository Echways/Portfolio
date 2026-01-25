from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from info.models import Achievement, News, Project, TeamMember


class ApiTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        now = timezone.now()
        cls.news = News.objects.create(
            title="API новость",
            slug="api-news",
            description="Описание новости для API",
            image="img/news/api.jpg",
            created_at=now,
        )
        cls.latest_news = News.objects.create(
            title="API новость 2",
            slug="api-news-2",
            description="Описание новости для API 2",
            image="img/news/api-2.jpg",
            created_at=now + timedelta(seconds=1),
        )
        cls.project = Project.objects.create(
            title="API проект",
            slug="api-project",
            description="Описание проекта для API",
            image="img/projects/api.jpg",
            created_at=now,
        )
        cls.latest_project = Project.objects.create(
            title="API проект 2",
            slug="api-project-2",
            description="Описание проекта для API 2",
            image="img/projects/api-2.jpg",
            created_at=now + timedelta(seconds=1),
        )
        cls.member = TeamMember.objects.create(
            name="API Member",
            skills="Django",
            order=1,
            is_active=True,
        )
        cls.achievement = Achievement.objects.create(text="API достижение")

    def test_api_root(self):
        response = self.client.get(reverse("api:root"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertIn("v1", data["versions"])

    def test_api_schema(self):
        response = self.client.get(reverse("api:schema"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["version"], "v1")

    def test_api_docs(self):
        response = self.client.get(reverse("api:docs"))
        self.assertEqual(response.status_code, 200)

    def test_news_list(self):
        response = self.client.get(reverse("api:news-list"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["page"], 1)
        self.assertGreaterEqual(data["count"], 2)
        self.assertEqual(data["results"][0]["slug"], self.latest_news.slug)

    def test_news_list_pagination(self):
        response = self.client.get(reverse("api:news-list") + "?page=1&page_size=1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["page_size"], 1)
        self.assertEqual(data["num_pages"], 2)
        self.assertIsNotNone(data["next"])

    def test_news_detail(self):
        response = self.client.get(reverse("api:news-detail", args=[self.news.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], self.news.title)

    def test_projects_list(self):
        response = self.client.get(reverse("api:projects-list"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreaterEqual(data["count"], 2)
        self.assertEqual(data["results"][0]["slug"], self.latest_project.slug)

    def test_team_list(self):
        response = self.client.get(reverse("api:team-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][0]["name"], self.member.name)

    def test_achievements_list(self):
        response = self.client.get(reverse("api:achievements-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["results"][0]["text"], self.achievement.text)
