from django.test import TestCase

from app.models import Post


class MyTestCase(TestCase):

    def setUp(self) -> None:
        self.post = Post.objects.create(name="this is a post.")

    def test_post(self):
        self.assertEqual(self.post.name, "this is a post.")

    def test_sum(self):
        self.assertEqual(20, (10 + 10))
