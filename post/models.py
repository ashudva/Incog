from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone

class Post(models.Model):
    author                  = models.ForeignKey(User, on_delete=models.CASCADE)
    confession              = models.TextField()
    heading                 = models.CharField(max_length=4000)
    pub_date                = models.DateTimeField('Date published')
    mod_date                = models.DateField('Date modified')
    appreciations           = models.PositiveIntegerField(default=0)
    views                   = models.PositiveIntegerField(default=0)
    n_comments              = models.IntegerField(default=0)

    def was_pub_recently(self):
        # return true if post is published before one day
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date

    # @classmethod
    # def create(cls, confession, heading):
    #     post =


    def __str__(self):
        return f"{self.id} - {self.heading}"


# Using tree nested comments will be implemented
# Below class is base class for comments and replies
class commentBase(models.Model):
    author                  = models.ForeignKey(User, on_delete=models.CASCADE)
    text                    = models.CharField(max_length=400)
    pub_date                = models.DateTimeField()
    mod_date                = models.DateField('Date modified')
    appreciations           = models.PositiveIntegerField(default=0)
    downvotes               = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Comment(commentBase):
    parent_post             = models.ForeignKey(Post, on_delete=models.CASCADE)
    n_replies               = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.id}. Comment: {self.text}, Replies: {self.n_replies}"

class Reply(commentBase):
    parent_comment          = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Replies'

    def __str__(self):
        return f"{self.id}. Reply: {self.text}"
