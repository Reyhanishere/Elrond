from django import forms
from .models import Article, Comment, Tag

class ArticleForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Use checkboxes for tags
        required=False  # Tags are optional
    )
    
class Meta:
    model = Article
    fields = ['title', 'content', 'tags']
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']