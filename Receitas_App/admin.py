from django.contrib import admin
from .models import Receita

class Listando_receitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_de_preparo', 'publicado')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicado',)
    list_per_page = 25


admin.site.register(Receita, Listando_receitas)


