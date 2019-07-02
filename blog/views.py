# -*-encoding=utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article


# Create your views here.
def hello(req):
    return HttpResponse("hello world^=^")

def article_content(req):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = "title: %s, brief_content: %s, content: %s, article_id: %s, publish_date: %s" % (title, brief_content, content, article_id, publish_date)
    return HttpResponse(return_str)

def get_index_page(req):
    page = req.GET.get("page")
    if page:
        page = int(page)
    else:
        page = 1
    articles = Article.objects.all()
    return render(req, 'blog/index.html', {
        "article_list": articles
    })

# def get_detail_page(req):
#     current_article = Article.objects.all()[0]
#     section_list = current_article.content.split("\n")
#     return render(req, 'blog/detail.html', {
#         "current_article": current_article,
#         "section_list": section_list
#     })

def get_detail_page(req, article_id):
    all_article = Article.objects.all()
    current_article = None
    previous_article = None
    next_article = None
    previous_index = 0
    next_index = 0
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            current_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = current_article.content.split("\n")
    return render(req, 'blog/detail.html', {
        "current_article": current_article,
        "section_list": section_list,
        "previous_article": previous_article,
        "next_article": next_article
    })