from django.conf.urls import url  #Import the Django function url
from . import views  #Import all our 'views' from the 'blog' application

urlpatterns = [
	
	#Assigning a view called post_list to the ^$ URL. 
	#This regular expression will match ^ (a beginning) followed by $ (an end) – so only an empty string will match. 	
	#That's correct, because in Django URL resolvers, 'http://127.0.0.1:8000/' is not a part of the URL. 
	#This pattern will tell Django that views.post_list is the right place to go if someone enters website at the 'http://127.0.0.1:8000/' address.
    url(r'^$', views.post_list, name='post_list'),  
	
	#it starts with ^ again – "the beginning".
	#post/ just means that after the beginning, the URL should contain the word post and a /. So far so good.
	#(?P<pk>\d+) – this part is trickier. It means that Django will take everything that you place here and transfer it to a view as a variable called pk. (Note that this matches the name we gave the primary key variable back in blog/templates/blog/post_list.html!) \d also tells us that it can only be a digit, not a letter (so everything between 0 and 9). + means that there needs to be one or more digits there. So something like http://127.0.0.1:8000/post// is not valid, but http://127.0.0.1:8000/post/1234567890/ is perfectly OK!
	#/ – then we need a / again.
	#$ – "the end"!
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

]#End URL Patterns



