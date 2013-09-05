# Create your views here.
from django.http import HttpResponse
from word_trees.models import Sentence, Word

from django.http import HttpResponse
from django.template import Context, loader

from django.core import serializers

def index(request):
    list = Sentence.objects.order_by('user_input')[:5]
    output1 = '  '.join([s.user_input for s in list])
    words = Word.objects.order_by('id')
    output2 = '  '.join([w.user_input for w in words])
    word = Word.objects.get(pk=1)
    words = Word.objects.filter(parent_id=word.id)
    output3 = '  '.join([w.user_input for w in words])
    output4 = buildTree(Word.objects.get(pk=1))
    print 'hello im in here'
    words = Word.objects.filter(parent_id=1)
    template = loader.get_template('word_trees/index.html')
    context = Context({
        'words': words,
        })
       
    return HttpResponse(output1+output2+output3+output4+template.render(context)) 
    

def detail(request, word_id):
    this_word = Word.objects.get(id=word_id)
    words = Word.objects.filter(parent_id=word_id)
    all_words = Word.objects.all()
    dict = {}
    
    for each in all_words:
        dict[each.id] = (each.user_input, each.parent_id)
        
    data = serializers.serialize("json", all_words)
        
    template = loader.get_template('word_trees/detail.html')
    firstWord = Word.objects.get(pk=3)
    tree = assembleTree(firstWord, [])
    
    context = Context({
        'this_word': this_word,
        'words': words,
        'all_words' : all_words,
        'dict' : dict,
        'data' : data,
        'tree' : tree,
        })
    return HttpResponse("this is sentence number %s." % word_id + template.render(context))

def assembleTree(firstWord, x):
    set = firstWord.word_set.all()
    lenSet = len(set)
    x.append(firstWord)  

    if lenSet > 0:   
        for each in set:           
            assembleTree(each, x)            
    return x    


        
    
    

def buildTree(ob):
        output = ''
        output += '-' + ob.user_input
        obs = Word.objects.filter(parent_id = ob.id)
        n = 1
        if obs:
            if n<5:
                output+=buildTree(Word.objects.get(pk=15))
#            for o in obs:
#                output += buildTree(o)
                output += 'see this?'
#                output += buildTree(obs[0])
                n+=1

        return output
    
    ####################
    
from django.views.generic.edit import CreateView
from word_trees.forms import SentenceForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

def sentence(request):
    if request.method == 'POST':
        form = SentenceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = SentenceForm()
    return render(request, 'word_trees/sentence.html', {
        'form': form,
    })
    

      