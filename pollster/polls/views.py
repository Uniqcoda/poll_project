from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Question, Choice
# Create your views here.

# Get questions and display them


def index(request):
    latest_questions = Question.objects.order_by('pub_date')
    paginator = Paginator(latest_questions, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'polls/index.html', {'latest_questions': page_obj})


# show specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})


# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# vote for a question choice
def vote(request, question_id):
    print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a user hits the back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
