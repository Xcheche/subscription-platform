from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages as message
from django.shortcuts import redirect
from writer.forms import ArticleForm
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
    
    return render(request, 'writer/create-article.html', {'form': form})