from django.conf.urls.defaults import *

from .views import IndexView, SearchView, DiffView, ListView, DetailView, CommitView, InsufficientPrivilegesView

urlpatterns = patterns('',
    (r'^$', IndexView(), {}, 'index'),
    (r'^search/$', SearchView(), {}, 'search'),
    (r'^diff/$', DiffView(), {}, 'diff'),
    (r'^list/$', ListView(), {}, 'list'),
    (r'^commit/$', CommitView(), {}, 'commit'),
    (r'^insufficient-privileges/$', InsufficientPrivilegesView(), {}, 'insufficient-privileges'),
    (r'^(?P<oxpid>\d{8})/$', DetailView(), {}, 'detail'),

)