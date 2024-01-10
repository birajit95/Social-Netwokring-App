from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    'rest fields are in Abstract User'

    # friends = models.ManyToManyField('self', through='FriendStatus')


    def get_friends(self):
        FriendStatus.objects.filter(status='accepted').values_list('friend')



class FriendStatus(models.Model):
    STATUS = (
        ('requested', 'requested'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected')
    )
    source_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends_set')
    target_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)





    
