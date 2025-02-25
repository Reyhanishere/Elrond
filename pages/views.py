from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.

# def homePageView(request):
#     return HttpResponse("Hello, World!")

class HomePageView(TemplateView):
    template_name = "homepage.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm()
    return render(request, 'articles/article_detail.html', {'article': article, 'comments': comments, 'form': form})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Set the author
            article.save()  # Save the article
            form.save_m2m()  # Save the many-to-many data (tags)
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'pages/create_article.html', {'form': form})

'''"Discuss Issues" (Q&A Section)'''

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'questions/question_list.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all()
    return render(request, 'questions/question_detail.html', {'question': question, 'answers': answers})