from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('policy.html', views.policy_view, name='policy.html'),
    path('contact.html', views.contact_view, name='contact.html'),
    path('submit-contact/', views.submit_contact_form, name='submit_contact'),
      
]