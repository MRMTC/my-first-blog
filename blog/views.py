from django.shortcuts import render, get_object_or_404
from django.utils import timezone
#The dot before models means current directory or current application. Both views.py and models.py are in the same directory. 
#This means we can use . and the name of the file (without .py). Then we import the name of the model (Post).
from .models import Post

# Create your views here.

#We created a function (def) called "post_list".
#It takes an input 'request' (from the user) and returns a function 'render' that will render/"put together" our template blog/post_list.html.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  #Name of our query set
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
	
