from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def index(request):
    """
    View for displaying the polls index.
    """
    return HttpResponse("Hello world. You're at the polls index.")

def detail(request, question_id):
    """
    View for displaying details of a specific question.
    """
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    """
    View for displaying results of a specific question.
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """
    View for voting on a specific question.
    """
    # Retrieve the question object from the database
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Retrieve the selected choice from the form data
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Increment the vote count for the selected choice
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect to the results page after successful voting
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

