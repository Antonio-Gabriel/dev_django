from django.contrib import admin
from django_app.models import Evento

# Register your models here.

class ShowEventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'usuario', 'data_criacao',)
    list_filter = ('titulo',)

admin.site.register(Evento, ShowEventoAdmin)