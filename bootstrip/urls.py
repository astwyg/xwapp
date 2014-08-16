from django.conf.urls import patterns, url ,include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from bs3.views import HomePageView, FormHorizontalView, FormInlineView, PaginationView, FormWithFilesView, \
    DefaultFormView, MiscView, DefaultFormsetView, DefaultFormByFieldView

from bootstrip import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$','bs3.views.myhome'),
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    url(r'^misc$', MiscView.as_view(), name='misc'),
    
    url(r'^iqtest$','iqtest.views.start_page'),
    url(r'^eqtest$','eqtest.views.start_page'),
    url(r'^agetest$','agetest.views.start_page'),
    url(r'^xznb_gostore$','xznb.views.xznb_gostore'),
    url(r'^xznb','xznb.views.xznb'),
    url(r'^discount_about$','xznb.views.discount_about'),
    url(r'^wxconfirm$','xznb.views.wxconfirm'),
    
    url(r'^get_info$','xznb.views.get_info'),
    url(r'^totb','totb.views.totb'),
)

# urlpatterns += patterns('django.views',
#     url(r'^css/(?P<path>.*)$', 'static.serve', 
#         {'document_root':settings.STATIC_ROOT+'css/'}),
#     url(r'^js/(?P<path>.*)$', 'static.serve', 
#         {'document_root':settings.STATIC_ROOT+'js/'}),
#     url(r'^image/(?P<path>.*)$', 'static.serve', 
#         {'document_root':settings.STATIC_ROOT+'image/'}),
# )