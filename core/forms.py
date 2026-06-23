from django import forms
import re
from .models import Driver, Putyovka, TIR, Dazvol, Litsenziya, IjaraShartnoma, Chiqim


class AdminLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'admin', 'class': 'input-field w-full px-4 py-3 rounded-xl text-sm'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••', 'class': 'input-field w-full px-4 py-3 rounded-xl text-sm'})
    )



class DriverLoginForm(forms.Form):
    telefon = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': '+998 90 123 45 67',
            'class': 'input-field w-full px-4 py-3 rounded-xl text-sm'
        })
    )

    parol = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': 'input-field w-full px-4 py-3 rounded-xl text-sm'
        })
    )

    def clean_telefon(self):
        telefon = self.cleaned_data['telefon']

        telefon = re.sub(r'\D', '', telefon)

        if len(telefon) == 9:
            telefon = '998' + telefon

        if telefon.startswith('998'):
            telefon = '+' + telefon

        return telefon

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['ism', 'telefon', 'mashina', 'raqam', 'parol', 'pasport_seriya']

        widgets = {
            'ism': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ism Familiya'
            }),
            'telefon': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+998901234567'
            }),
            'mashina': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'MAN TGX №...'
            }),
            'raqam': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'KRONE №...'
            }),
            'parol': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Haydovchi paroli'
            }),
            'pasport_seriya': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'AA 1234567'
            }),
        }

    def clean_telefon(self):
        telefon = self.cleaned_data['telefon']

        telefon = re.sub(r'\D', '', telefon)

        if len(telefon) == 9:
            telefon = '998' + telefon

        if telefon.startswith('998'):
            telefon = '+' + telefon

        return telefon


class PutyovkaForm(forms.ModelForm):
    class Meta:
        model = Putyovka
        fields = ['driver', 'raqam', 'shifr', 'narxi', 'tolangan', 'muddat',
                  'boshlanish', 'tugash', 'izoh']
        widgets = {
            'driver':     forms.Select(attrs={'class': 'form-input'}),
            'raqam':      forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'KRONE SD №402884CA'}),
            'shifr':      forms.TextInput(attrs={'class': 'form-input', 'placeholder': '1'}),
            'narxi':      forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '1000000'}),
            'tolangan':   forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '0'}),
            'muddat':     forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '12'}),
            'boshlanish': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'tugash':     forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'izoh':       forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }


class TIRForm(forms.ModelForm):
    class Meta:
        model = TIR
        fields = ['driver', 'tir_raqam', 'narxi', 'tolangan', 'muddat',
                  'boshlanish', 'tugash', 'izoh']
        widgets = {
            'driver':     forms.Select(attrs={'class': 'form-input'}),
            'tir_raqam':  forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'SCHMITZ №408748BA'}),
            'narxi':      forms.NumberInput(attrs={'class': 'form-input'}),
            'tolangan':   forms.NumberInput(attrs={'class': 'form-input'}),
            'muddat':     forms.NumberInput(attrs={'class': 'form-input'}),
            'boshlanish': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'tugash':     forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'izoh':       forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }


class DazvolForm(forms.ModelForm):
    class Meta:
        model = Dazvol
        fields = ['driver', 'mamlakat', 'dazvol_raqam', 'narxi', 'tolangan',
                  'boshlanish', 'tugash', 'izoh']
        widgets = {
            'driver':       forms.Select(attrs={'class': 'form-input'}),
            'mamlakat':     forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Rossiya, Germaniya...'}),
            'dazvol_raqam': forms.TextInput(attrs={'class': 'form-input'}),
            'narxi':        forms.NumberInput(attrs={'class': 'form-input'}),
            'tolangan':     forms.NumberInput(attrs={'class': 'form-input'}),
            'boshlanish':   forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'tugash':       forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'izoh':         forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }


class LitsenziyaForm(forms.ModelForm):
    class Meta:
        model = Litsenziya
        fields = ['driver', 'litsenziya_raqam', 'narxi', 'tolangan',
                  'boshlanish', 'tugash', 'izoh']
        widgets = {
            'driver':           forms.Select(attrs={'class': 'form-input'}),
            'litsenziya_raqam': forms.TextInput(attrs={'class': 'form-input'}),
            'narxi':            forms.NumberInput(attrs={'class': 'form-input'}),
            'tolangan':         forms.NumberInput(attrs={'class': 'form-input'}),
            'boshlanish':       forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'tugash':           forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'izoh':             forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }


class IjaraForm(forms.ModelForm):
    class Meta:
        model = IjaraShartnoma
        fields = ['driver', 'manzil', 'narxi', 'tolangan', 'boshlanish', 'tugash', 'izoh']
        widgets = {
            'driver':     forms.Select(attrs={'class': 'form-input'}),
            'manzil':     forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Qo\'qon, Mustaqillik ko\'chasi 12'}),
            'narxi':      forms.NumberInput(attrs={'class': 'form-input'}),
            'tolangan':   forms.NumberInput(attrs={'class': 'form-input'}),
            'boshlanish': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'tugash':     forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'izoh':       forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }


class ChiqimForm(forms.ModelForm):
    class Meta:
        model = Chiqim
        fields = ['driver', 'tur', 'summa', 'sana', 'izoh']
        widgets = {
            'driver': forms.Select(attrs={'class': 'form-input'}),
            'tur':    forms.Select(attrs={'class': 'form-input'}),
            'summa':  forms.NumberInput(attrs={'class': 'form-input'}),
            'sana':   forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'izoh':   forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }


class TolovForm(forms.Form):
    summa = forms.DecimalField(
        max_digits=12, decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '500000'})
    )
    izoh = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'To\'lov izohi'})
    )


