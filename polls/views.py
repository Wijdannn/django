from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from polls.models import Question,Choice
from django.views import generic

class Indexview(generic.ListView):
  model = Question
  context_object_name = 'latest_question_list'
  template_name = 'polls/index.html'

  def get_queryset(self):
    return Question.objects.order_by('-pub_date')[:5]
  
class Detailview(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
  model = Question
  template_name = 'polls/result.html'

def vote(request: HttpResponse, question_id:int):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError,Choice.DoesNotExist):
    return render(
      request,
      "polls/detail.html",
      {"question": question, "error_message": "you didn't select a choice"},

    )
  else:
    selected_choice.votes +=  1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:result", args=(question_id,)))