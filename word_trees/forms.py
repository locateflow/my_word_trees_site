from django import forms
from word_trees.models import Sentence

class SentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        