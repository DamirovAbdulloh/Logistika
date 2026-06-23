from django.contrib import admin
from .models import Driver, Putyovka, TIR, Dazvol, Litsenziya, IjaraShartnoma, Chiqim, TolovQayd

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'ism', 'telefon', 'mashina', 'raqam']
    search_fields = ['ism', 'telefon']

@admin.register(Putyovka)
class PutyovkaAdmin(admin.ModelAdmin):
    list_display = ['driver', 'raqam', 'narxi', 'tolangan', 'boshlanish', 'tugash', 'status']
    list_filter = ['status']
    search_fields = ['driver__ism']

@admin.register(TIR)
class TIRAdmin(admin.ModelAdmin):
    list_display = ['driver', 'tir_raqam', 'narxi', 'boshlanish', 'tugash', 'status']

@admin.register(Dazvol)
class DazvolAdmin(admin.ModelAdmin):
    list_display = ['driver', 'mamlakat', 'narxi', 'boshlanish', 'tugash', 'status']

@admin.register(Litsenziya)
class LitsenziyaAdmin(admin.ModelAdmin):
    list_display = ['driver', 'litsenziya_raqam', 'boshlanish', 'tugash', 'status']

@admin.register(IjaraShartnoma)
class IjaraAdmin(admin.ModelAdmin):
    list_display = ['driver', 'manzil', 'narxi', 'boshlanish', 'tugash']

@admin.register(Chiqim)
class ChiqimAdmin(admin.ModelAdmin):
    list_display = ['driver', 'tur', 'summa', 'sana']

@admin.register(TolovQayd)
class TolovQaydAdmin(admin.ModelAdmin):
    list_display = ['driver', 'tur', 'summa', 'sana']
