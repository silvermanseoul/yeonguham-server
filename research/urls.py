from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("researches/", views.ResearchList.as_view()),
    path("researches/<int:rid>/", views.ResearchDetail.as_view()),
    path("researches/<int:rid>/notice/", views.NoticeList.as_view()),
    path("researches/<int:rid>/notice/<int:nid>/", views.NoticeDetail.as_view()),
    path("researches/<int:rid>/ask/", views.AskList.as_view()),
    path("researches/<int:rid>/ask/<int:aid>/", views.AskDetail.as_view()),
    path("researches/search/", views.SearchList.as_view()),
    path("researches/field", views.FieldList.as_view()),
    path("recommendations/", views.RecommendList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
