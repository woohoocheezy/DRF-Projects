from importlib.resources import files
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        files = ('title', 'description', 'important')
        