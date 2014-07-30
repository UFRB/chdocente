from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView, TemplateView

from django.contrib import admin
admin.autodiscover()

from cadastro.views import RelatorioEnsino, RelatorioDocente, RelatorioProjetos
from cadastro.views import ExportarDisciplina, ExportarPesquisa
from cadastro.views import ExportarExtensao, ExportarAdministrativo
from cadastro.views import RelatorioCargaHoraria

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chdocente.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='admin/')),
    url(r'^relatorios/', TemplateView.as_view(template_name="relatorios.html")),
    url(r'^relatorio-ensino/', RelatorioEnsino),
    url(r'^relatorio-docente/', RelatorioDocente),
    url(r'^relatorio-projetos/', RelatorioProjetos),
    url(r'^relatorio-ch/', RelatorioCargaHoraria),
    url(r'^exportar-disciplina/', ExportarDisciplina, name="exportar-disciplina"),
    url(r'^exportar-pesquisa/', ExportarPesquisa, name="exportar-pesquisa"),
    url(r'^exportar-extensao/', ExportarExtensao, name="exportar-extensao"),
    url(r'^exportar-administrativo/', ExportarAdministrativo, name="exportar-admin"),
)
