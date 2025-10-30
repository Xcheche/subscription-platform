
from django.db import models
from accounts.models import CustomUser


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    is_premium = models.BooleanField(default=False,verbose_name="Is this a premium article?")
    date_posted = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title