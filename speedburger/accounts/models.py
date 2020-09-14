from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, User

# Create your models here.


'''
class UserManager(BaseUserManager):
    def create_user(self,username,phone,email,password):
        email = self.normalize_email(email)
        user = self.model(username=username,phone=phone,email=email)
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_superuser(self, username, phone, email, password):
        user = self.create_user(username=username, phone=phone ,email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
'''


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    adress = models.TextField()

    def __str__(self):
        return self.username


'''
    def create_user(self, username,phone,email,adress,password):
        user = User.objects.create_user(username=username,phone=phone,email=email,adress=adress,
        password=password)
        user.save()
'''
