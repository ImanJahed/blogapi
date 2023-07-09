from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Posts


# Create your tests here.
class PostsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', email='testuser@email.com', password='testpass1234')
        cls.post = Posts.objects.create(
            title='test title',
            content='test content for posts',
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEquals(self.post.author.username, 'testuser')
        self.assertEquals(self.post.title, 'test title')
        self.assertEquals(self.post.content, 'test content for posts')
        self.assertEquals(str(self.post), 'test title')
