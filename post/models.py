from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# class post(models.Model):
#     confession = ""
#     comments = {
#         "replies": 0,
#         "appreciate": 0,
#         "emojis": 0
#     }
#     owner = ""
#     reacts = {"appreciate": 0, "emojis": 0}

class Post(models.Model):
    confession              = models.CharField('Confession', max_length=4000)
    heading                 = models.CharField('Heading', max_length=4000)
    time                    = models.DateTimeField('Time published')
    appreciations           = models.PositiveIntegerField('Appreciations', default=0)
    views                   = models.PositiveIntegerField('Views', default=0)
    # import user from main or user model
    # author = models.Foreignkey(user.id, on_delete=models.CASCADE)

    def was_pub_recently(self):
        # return true if post is published before one day
        return timezone.now() - datetime.timedelta(days=1) <= self.post_time

    def __str__(self):
        return f"{self.id} - {self.confession} ----- {self.time}, {self.appreciations}"


# Using tree nested comments will be implemented
# Below class is base class for comments and replies
class commentBase(models.Model):

    text                    = models.CharField(max_length=400)
    time                    = models.DateTimeField('Timestamp')
    appreciations           = models.PositiveIntegerField('Appreciations', default=0)
    downvotes               = models.PositiveIntegerField('Downvotes', default=0)
    # import user from main or user model
    # author = models.Foreignkey(user, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Comment(commentBase):
    parent_post             = models.ForeignKey(Post, on_delete=models.CASCADE)
    replies                 = models.PositiveIntegerField('Replies', default=0)

    def __str__(self):
        return f"{self.id}. Comment: {self.text} ----- {self.time}, Appreciations: {self.appreciations}, Downvotes: {self.downvotes} replies: {self.replies}"

class Reply(commentBase):
    parent_comment          = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Replies'

    def __str__(self):
        return f"{self.id}. Reply: {self.text}, at: {self.time}, Appreciations: {self.appreciations}, Downvotes:{self.downvotes}"
