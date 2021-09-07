from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Blog
from django.urls import reverse


# Create your tests here.


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="admin1", email="admin1@email.com", password="pass"
        )

        self.blog = Blog.objects.create(
            Name="appleBlog", Message="test",description="good", author=self.user,
        )

    def test_string_representation(self):
            self.assertEqual(str(self.blog), "appleBlog")
    
    def test_snack_list_view(self):
        response = self.client.get(reverse("Blogs_list"))
        self.assertEqual(response.status_code, 403)
        # self.assertContains(response, "appleBlog")
        # self.assertTemplateUsed(response, "snack_list.html")