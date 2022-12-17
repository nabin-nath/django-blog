from django.shortcuts import render

# Create your views here.
def article_list(requests):
    return render(requests, 'article/article_list.html')
