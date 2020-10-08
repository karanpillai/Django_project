from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #OneToOne means every user will have one Profile and vice versa
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Cascade means agar user delete hua toh profile delete hoga.
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    state = models.CharField(max_length=100)

    def __str__(self):
        return f'{ self.user.username } Profile'