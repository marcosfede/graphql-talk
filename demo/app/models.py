from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=None)
    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='posts')


class Comment(models.Model):
    text = models.TextField(max_length=400)
    post = models.ForeignKey('Post', related_name='comments',
                             on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name='comments')