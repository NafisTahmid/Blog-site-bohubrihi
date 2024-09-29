from django import forms
from App_Blog.models import Blog, Comment, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_content', 'blog_image')

        widgets = {
            'blog_title':forms.TextInput(attrs=({'class':'form-control'})),
            'blog_content':forms.Textarea(attrs=({'class':'form-control'})),
            'category':forms.Select(choices=choice_list,attrs=({'class':'form-control'})),
            'blog_image':forms.FileInput(attrs=({'class':'form-control'}))

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)