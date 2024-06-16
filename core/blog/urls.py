from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = "blog"

urlpatterns = [
    # path("", TemplateView.as_view(template_name="index.html",extra_context={"name":"mohsen"})),
    path("1", views.Indexview.as_view(),name='1')
]