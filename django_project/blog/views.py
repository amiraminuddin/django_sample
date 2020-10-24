from django.shortcuts import render
#from django.http import HttpResponse 

#this one is dummy data
posts = [
    {
        'author':'don',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'October 23, 2020'
    },
    {
        'author':'pekeh',
        'title':'Blog post 2',
        'content':'second post content',
        'date_posted':'October 24, 2020'
    }
]

# Create your views here.
def home(request):

    #dictionary for data posts
    context = {
        'title': 'welcome',
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

