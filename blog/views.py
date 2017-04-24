from django.shortcuts import render

# Create your views here.

#We created a function (def) called "post_list".
#It takes an input 'request' and returns a function 'render' that will render/"put together" our template blog/post_list.html.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
	
	
