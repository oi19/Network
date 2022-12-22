from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.files import ImageField


class User(AbstractUser):
    pass

    # def __str__(self):
    #     return self.user


class Post(models.Model):
    creator = models.ForeignKey(
        "User", on_delete=models.PROTECT, related_name="posts")
    body = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField("User", related_name="likes")
    likes_counter = models.IntegerField(default=0)


class Followers(models.Model):
    followee = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="followers")
    following = models.ForeignKey(
        "User", on_delete=models.PROTECT, related_name="following")

    def serialize(self):
        return {
            'user': self,
            "id": self.id,
            "creator": self.creator,
            # "recipients": [user.email for user in self.recipients.all()],
            # "subject": self.subject,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%m/%d/%Y"),
            "likes_counter": self.likes_counter,
            # "archived": self.archived
        }
