#==Imports==
from django.db import models
from django.utils import timezone


#==Class Definitions==

#Post = name of our Model i.e. its the Class name
#models.Model == Means that Post is a Django Model.  So Django knows it should be saved in the DB.
class Post(models.Model):
    author = models.ForeignKey('auth.User')  	 
    title = models.CharField(max_length=200)  #Char[200]
    text = models.TextField()  #Long text with no limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)  
    #If a string-based field has null=True, that means it has two possible values for “no data”: NULL, and the empty string.
    #For both string-based and non-string-based fields, you will also need to set blank=True if you wish to permit empty values in forms, as the null parameter only affects database storage (see blank).  

    #Publish method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
