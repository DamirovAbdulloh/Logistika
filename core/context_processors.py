from datetime import date
from .models import Putyovka, TIR, Dazvol


def expired_docs_count(request):
    """Sidebar'dagi qizil belgi uchun — muddati tugagan hujjatlar soni.
    Faqat admin tizimga kirgan bo'lsa hisoblanadi, aks holda ortiqcha so'rov yubormaymiz."""
    if not (request.user.is_authenticated and request.user.is_staff):
        return {}

    today = date.today()
    count = 0
    count += Putyovka.objects.filter(tugash__lt=today, status='faol').count()
    count += TIR.objects.filter(tugash__lt=today).exclude(status='tugagan').count()
    count += Dazvol.objects.filter(tugash__lt=today).exclude(status='tugagan').count()

    return {'expired_count': count}
