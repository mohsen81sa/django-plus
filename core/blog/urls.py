from django.urls import path
from django.views.generic import TemplateView,RedirectView
from . import views
app_name = "blog"

urlpatterns = [
    # path("", TemplateView.as_view(template_name="index.html",extra_context={"name":"mohsen"})),
    path("blog-index", views.Indexview.as_view(),name='index'),
    path("go-to-index",RedirectView.as_view(pattern_name="blog:index"),name="go-to-index")
]