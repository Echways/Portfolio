from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from info.models import Achievement, News, Project, TeamMember


class InfoPagesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        base_time = timezone.now()
        cls.achievement = Achievement.objects.create(text="Первое достижение")
        cls.team_member = TeamMember.objects.create(
            name="Admin",
            skills="Python, Django",
            telegram_url="https://t.me/example",
            instagram_url="https://instagram.com/example",
            order=1,
            is_active=True,
        )
        cls.news = News.objects.create(
            title="Первая новость",
            description="Описание новости",
            image="img/news/test.jpg",
            created_at=base_time,
        )
        cls.project = Project.objects.create(
            title="Первый проект",
            description="Описание проекта",
            image="img/projects/test.jpg",
            created_at=base_time,
        )
        for i in range(2, 8):
            News.objects.create(
                title=f"Новость {i}",
                description=f"Описание новости {i}",
                image=f"img/news/test-{i}.jpg",
                created_at=base_time + timedelta(seconds=i),
            )
            Project.objects.create(
                title=f"Проект {i}",
                description=f"Описание проекта {i}",
                image=f"img/projects/test-{i}.jpg",
                created_at=base_time + timedelta(seconds=i),
            )
        cls.newest_news_title = "Новость 7"
        cls.newest_project_title = "Проект 7"

    def test_info_page_status_and_template(self):
        response = self.client.get(reverse("info:info"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/infopage.html")
        self.assertContains(response, self.achievement.text)
        self.assertContains(response, self.team_member.name)

    def test_news_list_page(self):
        response = self.client.get(reverse("info:news"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/news.html")
        self.assertContains(response, self.newest_news_title)
        self.assertNotContains(response, self.news.title)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(response.context["paginator"].num_pages, 2)

    def test_projects_list_page(self):
        response = self.client.get(reverse("info:projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/projects.html")
        self.assertContains(response, self.newest_project_title)
        self.assertNotContains(response, self.project.title)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(response.context["paginator"].num_pages, 2)

    def test_news_detail_page(self):
        response = self.client.get(reverse("info:news-detail", args=[self.news.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/newspost_dl.html")
        self.assertContains(response, self.news.title)
        self.assertContains(response, self.news.description)

    def test_project_detail_page(self):
        response = self.client.get(reverse("info:project-detail", args=[self.project.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "info/projectpost_dl.html")
        self.assertContains(response, self.project.title)
        self.assertContains(response, self.project.description)

    def test_detail_pages_404(self):
        news_response = self.client.get(reverse("info:news-detail", args=["missing"]))
        project_response = self.client.get(reverse("info:project-detail", args=["missing"]))
        self.assertEqual(news_response.status_code, 404)
        self.assertEqual(project_response.status_code, 404)

    def test_news_pagination_second_page_contains_oldest(self):
        response = self.client.get(reverse("info:news") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.news.title)

    def test_projects_pagination_second_page_contains_oldest(self):
        response = self.client.get(reverse("info:projects") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.title)
