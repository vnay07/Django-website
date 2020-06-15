from .models import Comment
from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body',)#Now it is a tuple earlier i.e ('body') is a string
        