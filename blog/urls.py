from django.conf.urls import url  #Import the Django function url
from . import views  #Import all our 'views' from the 'blog' application

urlpatterns = [
	
	#Assigning a view called post_list to the ^$ URL. 
	#This regular expression will match ^ (a beginning) followed by $ (an end) – so only an empty string will match. 	
	#That's correct, because in Django URL resolvers, 'http://127.0.0.1:8000/' is not a part of the URL. 
	#This pattern will tell Django that views.post_list is the right place to go if someone enters website at the 'http://127.0.0.1:8000/' address.
    url(r'^$', views.post_list, name='post_list'),  

]#End URL Patterns



