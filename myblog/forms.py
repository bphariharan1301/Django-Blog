from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sectumsempra Spell'}),
            'author' : forms.Select(attrs={'class':'form-control', 'placeholder':'Severus Snape'}),
            'body' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'For enemies'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sectumsempra Spell'}),
            'body' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'For enemies'}),
        }
