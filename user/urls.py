from django.conf.urls import url

from user.views import (
    UserListView,
    UserDeleteView,
    UserCreateView,
    UserUpdateView,
    UserDetailView
)

app_name = 'user'

urlpatterns = [
    url(
        r'^update/(?P<email>[\w.@+-]+)/$',
        UserUpdateView.as_view(),
        name='update-user'
    ),
    url(
        r'^delete/(?P<email>[\w.@+-]+)/$',
        UserDeleteView.as_view(),
        name='delete-user'
    ),
    url(
        r'^create/$',
        UserCreateView.as_view(),
        name='create-user'
    ),
    url(
        r'^(?P<email>[\w.@+-]+)/$',
        UserDetailView.as_view(),
        name='get-user'
    ),
    url(r'^$', UserListView.as_view(), name='users-list'),
]
