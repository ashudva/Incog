from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    # username, first_name, last_name, email will be taken from User model
    # profile_picture, add multiple options like favs, interests, follow, followers option to added later
    owner               = models.OneToOneField(User, on_delete = models.CASCADE)
    PRIVATE             = 'PR'
    PUBLIC              = 'PB'
    COMMUNITIES         = 'CM'
    visibility          = [
        (PRIVATE, 'private'),
        (PUBLIC, 'public'),
        (COMMUNITIES, 'Communities'),
    ]
    profile_visibility  = models.CharField(
        max_length      = 2,
        choices         = visibility,
        default         = PUBLIC,
    )
    birth_date          = models.DateField(blank=True, null=True)
    dream               = models.TextField(max_length=400, blank=True)
    ambition            = models.TextField(max_length=400, blank=True)
    bio                 = models.TextField(max_length=400, blank=True)
    status              = models.CharField(max_length=200, blank=True)
    philosophy          = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f"Profile of {self.owner}"
