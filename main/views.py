from django.shortcuts import render,redirect
from . models import Courses,Video, Comment
from math import ceil
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from validate_email import validate_email

from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def courses(request):
    allCourse = []
    catCourse = Courses.objects.values('category', 'id')
    cats = {item['category']for item in catCourse}

    for cat in cats:
        course = Courses.objects.filter(category = cat)
        n = len(course)
        #Display 4 Courses in a row
        nSlides = n//4 + ceil((n/4)-(n//4))
        allCourse.append([course, range(1, nSlides), nSlides])
    params = {'allCourse':allCourse}
    return render(request,'main/course.html',params)


#for below classes we have this function which will have title of all the videos
def courseView(request, cat):
    dict = {'videos':Video.objects.filter(v_category=cat) }
    return render(request,'main/material.html',dict)

#I Will create some classes to display our Videos
#For this we have Different View in Django
#import:  from django.views.generic import ListView

class VideoListView(ListView):
    model = Video
    template_name = 'main/material.html'
    context_object_name = 'videos'
    paginate_by = 6

    def get_queryset(self):
        #self.v_category = get_object_or_404(Video, v_category = self.kwargs.get('cat'))
        return Video.objects.filter(v_category = self.kwargs.get('cat')).order_by('v_pubDate')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Video, pk=pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, f'Comment is recorded!')
            return redirect('videoListView', cat=post.v_category)
    else:
        form = CommentForm()
    return render(request, 'main/add_comment_to_post.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        mail = request.POST['email']
        subject = request.POST['subject']
        is_valid = validate_email(mail, verify=True)
        if is_valid == True:
            send_mail(
                subject,
                message,
                mail,
                [settings.EMAIL_HOST_USER],
                fail_silently=False
            )
            messages.success(request, 'Your Message has been successfully send!!!')
        else:
            messages.warning(request, 'Enter a valid Email!!!')
    return render(request,'main/contact.html')

