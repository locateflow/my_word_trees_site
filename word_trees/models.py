from django.db import models

class Sentence(models.Model):
    user_input = models.CharField(max_length=300)
    
    def __unicode__(self):
        return self.user_input
    
    def words(self):
        return self.user_input.split()
    
    def get_words(self):
        words = self.words()
        last_w = Word.objects.get(pk=1)
        
        for word in words:
            child_query = Word.objects.filter(parent = last_w, user_input = word)
            if child_query:
                last_w = child_query.get()
            else:
                w = Word(user_input=word, sentence=self, parent = last_w)
                w.save()
                last_w = w
            
    
        
        
    
class Word(models.Model):
    sentence = models.ForeignKey(Sentence, null=True)
    user_input = models.CharField(max_length=50)
#    parent_id = models.IntegerField(default=0)
    parent = models.ForeignKey('self', null=True)
    

    def __unicode__(self):
        return self.user_input  

from django.forms import ModelForm

class SentenceForm(ModelForm):
    class Meta:
        model = Sentence
        