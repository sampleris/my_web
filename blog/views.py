from django.shortcuts import render
from .models import Post
posts = [

    {
        'author': ' Mpara Romaric',
        'title': 'Blog post1',
        'content': 'First post content',
        'date_posted': 'February 25, 2023'

},
{
 
        'author': 'Carine',
        'title': 'Blog post2',
        'content': 'second post content',
        'date_posted': 'February 28, 2023'   
},
{
    'author': 'Faith',
        'title': 'Blog post3',
        'content': 'Third post content',
        'date_posted': 'February 28, 2023'   
}


]
#Post.objects.all() is to load posts from the database
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
def bootstrap(request):
    return render(request, 'blog/' )
def register(request):
    return render(request, 'users/register.html')


# Create your views here.