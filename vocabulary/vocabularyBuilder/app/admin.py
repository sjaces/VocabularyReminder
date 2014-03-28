from django.contrib import admin
from app.models import Diccionario, Palabra


# Register your models here.

class DiccionarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'jugada', 'fecha_ultima_jugada')
    list_filter = ('usuario',)
class PalabraAdmin(admin.ModelAdmin):
    list_display = ('diccionario', 'palabra_A',
            'palabra_B', 'jugada_proxima')
    list_filter = ('diccionario',)
    search_fields = ('palabra_A', 'palabra_B', 
                'diccionario__nombre',)

admin.site.register(Diccionario, DiccionarioAdmin)
admin.site.register(Palabra, PalabraAdmin)