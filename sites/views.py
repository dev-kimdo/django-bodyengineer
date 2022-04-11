from django.shortcuts import render

from posts.models import Post

# Create your views here.
def main(request):
    posts = Post.objects.all()

    content = {
        'posts' : posts
    }
    return render(request, 'sites/bodyengineer.html', content)

def about(request):
    return render(request, 'sites/abouts.html')

def map(request):
    return render(request, 'sites/map.html')