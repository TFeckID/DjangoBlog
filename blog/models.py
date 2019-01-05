from django.db import models
from DjangoUeditor.models import *
# Create your models here.

class Artical(models.Model):

    title = models.CharField(u'博客标题',max_length=50)
    category = models.CharField(u'博客标签',max_length=20,blank=True)
    pub_date = models.DateTimeField(u'发布日期',auto_now_add=True,editable=True)
    update_date = models.DateTimeField(u'修改时间',auto_now=True,null=True)
    #content = models.TextField(blank=True,null=True) #博客正文

    content = UEditorField(u"文章正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '文章'
        verbose_name_plural = '文章'