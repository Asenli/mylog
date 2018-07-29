from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        #返回名字
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    content = RichTextUploadingField(blank=True,null=True,verbose_name="内容")
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    readed_num = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Blog:%s>'% self.title

    class Meta:
        ordering = ['-created_time']



        