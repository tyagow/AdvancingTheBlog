from django.conf.urls import url

from .views import (
	comment_detail,
	comment_delete,
)

urlpatterns = [
	url(r'^(?P<id>\d+)/$', comment_detail, name='comment_detail'),
	url(r'^(?P<id>\d+)/delete/$', comment_delete, name='comment_delete'),
]
