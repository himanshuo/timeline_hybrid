from django.db import models
from djangotoolbox.fields import ListField
from django_mongodb_engine.contrib import MongoDBManager


from djangotoolbox.fields import EmbeddedModelField


#PG
class Timeline(models.Model):


    #the parameters to the models are:
        #max_length - max length we allow varchar
        #null - makes it so blank values are stored as null in database.
        #default  - default value given to a value. None=null in database
        #blank - allowed to be blank in terms of validation when True.
            # if blank, then null=True will make it null in db
    title = models.CharField(max_length=256, null=True, blank=True)#null= makes it so blank values are stored as null which is what you want.
    author = models.CharField(max_length=256, null=True,blank=True)
    wiki = models.TextField(max_length=256, null=True, blank=True)
    project_id = models.IntegerField(blank=False, null=False)#cant be empty
    #version = models.IntegerField()
    date = models.DateTimeField(blank=False)#cant be empty since by default blank=False(+specified)

    #class Meta:
    #    ordering = ['project_id', '-date']#awesome optimization that keeps your timeline sorted. cant use though in benchmarking.:(


#MONGO
class History(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)#null= makes it so blank values are stored as null which is what you want.
    author = models.CharField(max_length=256, null=True,blank=True)
    wiki = models.TextField(max_length=256, null=True, blank=True)

    date = models.DateTimeField()
    project_id = models.IntegerField(blank=False, null=False)
    class MongoMeta:
        ordering = ['-date']


    #can use raw_update to create your specific updates in the future for when you add in a new timeline, and the current
    #needs to go into history


