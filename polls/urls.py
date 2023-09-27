from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
  path('',views.Indexview.as_view(),name='index'),
  path('<int:pk>/', views.Detailview.as_view(), name="detail"  ),
  path('<int:pk>/result/', views.ResultView.as_view(), name="result"  ),
  path('<int:question_id>/vote/', views.vote, name="vote"  ),
]