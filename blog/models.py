from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)    #add_now = post updat karne par current date daalega and auto_now_add = shuru ka date fix hoga
    author = models.ForeignKey(User,on_delete=models.CASCADE)   #on_delete matlab user delete ho gaya toh post bhi delete ho jayga

    def __str__(self):
        return self.title
"""
Shell commands
User.objects.all()
User.objects.first()/ User.objects.last()
User.objects.filter(username = 'karan')
user = User.objects.filter(username = 'karan')
user.id / user1.pk
User.objects.get(id = 1)

post1 = Post(title='',content='',author = user)
post1.save()

"""