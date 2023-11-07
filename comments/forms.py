from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

    def clean_body(self):
        body = self.cleaned_data.get('body').lower()
        bad_comments = ['ерунда', 'чушь', 'хлам']
        for c in bad_comments:
            if c in body:
                raise ValidationError('Комментарий не прошел автомодерацию!')
        return body
