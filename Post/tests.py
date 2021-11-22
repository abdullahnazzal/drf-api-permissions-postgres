from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.fields import DateTimeField
from rest_framework.test import APITestCase
from django.db import models

from .models import Post

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Post.objects.create(
            author = test_user,
            title = 'Title of Blog',
            body = 'Words about the blog'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_author = f"{post.author}"
        expected_title = f"{post.title}"
        expected_body = f"{post.body}"
        self.assertEqual(expected_author, "tester")
        self.assertEqual(expected_title, "Title of Blog")
        self.assertEqual(expected_body, "Words about the blog")