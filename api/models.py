from django.db import models
import time
# Create your models here.


class Trip(models.Model):
    id = models.AutoField(primary_key=True)       #唯一ID,
    trip_title = models. CharField(max_length=100)        #标题,
    trip_subtitle = models.CharField(max_length=100)         #副标题,
    cover = models.TextField()                       #封面照片名称
    pub_time = models.DateTimeField('date published')   #时间,
    place = models.CharField(max_length=100)         #地点,
    likeCount = models.IntegerField(default=0)           #赞的数量

    def __str__(self):              # __unicode__ on Python 2
        return self.trip_title


    def toDict(self):
        #datatime时间不能直接发送，需要先转成时间戳再格式化为字典
        tmstp = int(time.mktime(self.pub_time.timetuple()))
        return {
        'trip_title':self.trip_title,
        'trip_subtitle':self.trip_subtitle,
        'cover':self.cover,
        'place':self.place,
        'likeCount':self.likeCount,
        'pub_time' : tmstp,
        'day_Count' : self.day_set.count() #获取Trip对应的日程数量
        }


class Day(models.Model):
    id = models.AutoField(primary_key=True)       #唯一ID,
    trip_title = models.CharField(max_length=100)         #标题,
    trip_subtitle = models.CharField(max_length=100)         #副标题,
    trip_day = models.IntegerField(default=1)           #旅行日期,
    cover = models.TextField()                       #封面照片名称
    pub_time = models.DateTimeField('date published')   #时间,
    place = models.CharField(max_length=100)         #地点,
    likeCount = models.IntegerField(default=0)           #赞的数量,
    content = models.TextField()                       #日记内容,
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)                  #对应的旅程

    def __str__(self):              # __unicode__ on Python 2
        return self.trip_title