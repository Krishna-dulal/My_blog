from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import ContactForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def policy_view(request):
    return render(request, 'policy.html')

def contact_view(request):
    return render(request, 'contact.html')

def submit_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data and perform actions (e.g., send an email)
            # Redirect to a thank you page or display a success message
            return HttpResponseRedirect('/thank-you/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})