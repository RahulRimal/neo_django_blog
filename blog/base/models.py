from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=200, null=False)
    desc = models.TextField(blank=True)
    # image = 
    posted_on = models.DateTimeField(auto_now_add=True)
    # post_comment = models.ForeignKey(Comment, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

