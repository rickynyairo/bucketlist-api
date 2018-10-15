"""
url patterns for the bucketlist api
"""

from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = {
    # url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    path('bucketlists/', CreateView.as_view(), name="create"),
    path('bucketlist/<int:pk>/', DetailsView.as_view(), name='details')
}

urlpatterns = format_suffix_patterns(urlpatterns)