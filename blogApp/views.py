from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic

# Create your views here.
def index(request):
    text = {'text': 'World'}
    return render(request, 'blogApp/index.html', {'t': text})

def detail(req):
    return render(req, 'blogApp/detail.html')


class PageView(generic.ListView):
    template_name = 'blogApp/page.html'
    '''
    对于 ListView， 自动生成的 context 变量是 question_list。
    为了覆盖这个行为，我们提供 context_object_name 属性，表示我们想使用 content
    '''
    context_object_name = 'content'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# DetailView 期望从 URL 中捕获名为 "pk" 的主键值，所以我们为通用视图把 question_id 改成 pk
class DtView(generic.DetailView):
    model = Question
    '''
    对于 DetailView ， question 变量会自动提供—— 因为我们使用 Django 的模型 (Question)，
     Django 能够为 context 变量决定一个合适的名字
    '''
    template_name = 'blogApp/dt.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blogApp/results.html'

def page(request):
    latest_question_list = Question.objects.order_by('-pub_date')[0:5]
    return render(request, 'blogApp/page.html', {'content': latest_question_list})

def dt(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blogApp/dt.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blogApp/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'blogApp/dt.html', {'question': question, 'message_error': 'no data'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('blog:result', args=(question_id,)))