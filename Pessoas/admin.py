from django.contrib import admin
from .models import Pessoa

class Listando_pessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome', 'email')
    search_fields = ('nome', 'email')
    list_per_page = 25

admin.site.register(Pessoa, Listando_pessoas)
