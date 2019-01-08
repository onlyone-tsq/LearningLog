from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    #用户学习的主题
    #需要存储少量的文本时，可以使用字段CharField
    text = models.CharField(max_length=200)
    #需要记录日期和时间时，可以使用字段DateTimeField
    #auto_now_add=True表示每当创建新主题时，都会使用当前日期和时间
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        #返回模型中 存储的字符串
        return self.text

class Entry(models.Model):
    #学习到的某个主题 的相关条目
    #ForeignKey外键，此处表示引用数据库Topic表记录，使每个条目都关联到相应的主题
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    #TextField实例，特点是不限制文本长度
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        #存储用于管理模型的额外信息,Django使用entries来表示多个条目
        verbose_name_plural = 'entries'

    def __str__(self):
        #只显示前50个条目的text
        return self.text[:50] + "..."