from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=50)
    Token = models.CharField(max_length=100)
    Slug = models.SlugField(unique=True)
    Content=models.TextField(validators=[MinLengthValidator(10)])
    Image = models.ImageField(upload_to="Imgs",null=True)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateField(auto_now=True)
    