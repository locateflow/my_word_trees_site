from django.contrib import admin
from word_trees.models import Sentence, Word

#admin.site.register(Sentence)

class WordInline(admin.StackedInline):
    model = Word
    extra = 3


class SentenceAdmin(admin.ModelAdmin):
#    fields = ['user_input']
#    inlines = [WordInline]
    list_display = ('user_input', 'words')

    
class WordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['user_input']}), 
        ('Ancestry',{'fields': ['parent', 'sentence'], 'classes': ['collapse']}),
    ]

admin.site.register(Sentence, SentenceAdmin)
admin.site.register(Word, WordAdmin)