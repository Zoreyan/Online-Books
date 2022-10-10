from django.forms import ModelForm, CheckboxInput, TextInput, FileInput,Textarea, EmailInput
from .models import Book, FeedBack


class BookForm(ModelForm):
    class Meta:

        model = Book
        fields = ['title', 'description', 'image', 'author', 'category', 'language', 'file', 'writed']
        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'id':'title'
            }),
            'author':TextInput(attrs={
                'class':'form-control',
                'id':'author'
            }),
            'description':Textarea(attrs={
                'class':'form-control',
                'id':'description'
            }),
            # 'language':RadioSelect(attrs={'class':'form-check-input', 'id':'language', 'type':'radio','checked':"",'name':'languageSelect'}),
            'image':FileInput(attrs={
                'class':'form-control',
                'type':'file',
                'id':'image'
            }),
            'file':FileInput(attrs={
                'class':'form-control',
                'type':'file',
                'id':'file'
            }),
            'writed':TextInput(attrs={

                'type':'text'
            })

        }


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ['email', 'text']
        widgets = {
            'email':EmailInput(attrs={
                'class':'form-control',
                'id':'email',
                'required':''
            }),
            'text':Textarea(attrs={
                'class':'form-control',
                'id':'text',
                'required':''
            }),
        }