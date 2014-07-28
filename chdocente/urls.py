from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

from cadastro.views import RelatorioEnsino, RelatorioDocente
from cadastro.views import ExportarDisciplina, ExportarPesquisa
from cadastro.views import ExportarExtensao, ExportarAdministrativo

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chdocente.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='admin/')),
    url(r'^relatorio-ensino/', RelatorioEnsino),
    url(r'^relatorio-docente/', RelatorioDocente),
    url(r'^exportar-disciplina/', ExportarDisciplina),
    url(r'^exportar-pesquisa/', ExportarPesquisa),
    url(r'^exportar-extensao/', ExportarExtensao),
    url(r'^exportar-administrativo/', ExportarAdministrativo),
)
