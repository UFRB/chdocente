from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

from cadastro.views import RelatorioEnsino, RelatorioDocente
from cadastro.views import ExportarDisciplinas, ExportarPesquisas

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chdocente.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='admin/')),
    url(r'^relatorio-ensino/', RelatorioEnsino),
    url(r'^relatorio-docente/', RelatorioDocente),
    url(r'^exportar-disciplinas/', ExportarDisciplinas),
    url(r'^exportar-pesquisas/', ExportarPesquisas),
)
