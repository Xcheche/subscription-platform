from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages as message
from django.shortcuts import redirect
from urllib3 import request
from writer.forms import ArticleForm
from .models import Article
# Create your views here.

@login_required
def writer_dashboard(request):
   
    return render(request, 'writer/writer-dashboard.html')

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # Save the article but don't commit to the database yet
            article = form.save(commit=False)
            # Assign the current user as the author
            article.user = request.user
            article.save()
            message.success(request, "Article created successfully!")
            #return  HttpResponse("Article created successfully!")
            return redirect('writer-dashboard')
        #  or return redirect to another page
    else:
        form = ArticleForm()
    
    return render(request, 'writer/my-articles.html', {'form': form})


#Article list of the user
@login_required 
def article_list(request):
    current_user = request.user.id
    articles = Article.objects.filter(user=current_user).order_by('-date_posted')
    return render(request, 'writer/my-articles.html', {'articles': articles})