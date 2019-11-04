from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    # username, first_name, last_name, email will be taken from User model
    # profile_picture, add multiple options like favs, interests, follow, followers option to added later
    owner               = models.ForeignKey(User, on_delete = models.CASCADE)
    PRIVATE             = 'PR'
    PUBLIC              = 'PB'
    COMMUNITIES         = 'CM'
    visibility        = [
        (PRIVATE, 'private'),
        (PUBLIC, 'public'),
        (COMMUNITIES, 'Communities'),
    ]
    profile_visibility  = models.CharField(
        max_length      = 2,
        choices         = visibility,
        default         = PUBLIC,
    )
    dream               = models.CharField(max_length=600, blank=True)
    ambition            = models.CharField(max_length=600, blank=True)
    bio                 = models.CharField(max_length=600, blank=True)
    status              = models.CharField(max_length=600, blank=True)
    philosophy          = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return f"Profile of {self.owner}"
