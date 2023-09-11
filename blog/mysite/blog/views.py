from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post
from .forms import ContactForm
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def policy_view(request):
    """View for the policy page."""
    return render(request, 'policy.html')

def contact_view(request):
    """View for the contact page."""
    return render(request, 'contact.html')

def submit_contact_form(request):
    """View for submitting the contact form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            # You can add your processing logic here

            # Display a success message using Django's messages framework
            messages.success(request, 'Your message was sent successfully!')
            return redirect('thank_you')  # Use the named URL pattern
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
