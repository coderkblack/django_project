from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

posts = [
    {
    "id": 0,
     "title": "Let's explore python",
     "content": "Python is interpreted, high level, general purpose programming language. Wiidely used in the fields of web development, data science and machine learning."
     },
     {
       "id": 1,
       "title": "Django the best web framework",
       "content": "Django is used by almost every big tech company like facebook, google, youtube, instagram etc"  
     },
     {
         "id": 2,
         "title": "Let's explore Javascript",
         "content": "Javascript is interpreted, high level, general purpose programming language. Widely used in the fields of web develpoment."
     }
]


# function based views(FBVs)

def home(request):
    html = ""
    for post in posts:
        html += f'''
            <div>
            <a href="/post/{post["id"]}">
                <h1>{post['id']} - {post['title']}</h1></a>
                <p>{post['content']}</p>
            </div>
'''
    name = "Jeff Bezos"
    return render(request, 'posts/home.html', {"posts": posts, "username": "taranjot"})

def post(request, id):
    valid_id = False
    for post in posts:
        if post["id"] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:    
        html = f'''
            <h1>{post_dict['title']}</h1>
            <p>{post_dict['content']}</p>
        '''
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("Post Not Available")


# def post2(request, id):
    for post in posts:
        if post['id'] == id:
            post_dict = post
            break
    html = f'''
    <h1>{post_dict['title']}</h1>
    <p>{post_dict['content']}</p>
''' 
    return HttpResponse(html)

def google(request, id):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)