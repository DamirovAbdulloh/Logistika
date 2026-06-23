from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


class Driver(models.Model):
    """Haydovchi profili"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='driver_profile')
    ism = models.CharField(max_length=200, verbose_name="Ism Familiya")
    telefon = models.CharField(max_length=20, verbose_name="Telefon")
    mashina = models.CharField(max_length=200, blank=True, verbose_name="Mashina")
    raqam = models.CharField(max_length=100, blank=True, verbose_name="Davlat raqami")
    parol = models.CharField(max_length=100, blank=True, verbose_name="Parol (oddiy)")
    pasport_seriya = models.CharField(max_length=50, blank=True, verbose_name="Pasport seriya raqami")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Haydovchi"
        verbose_name_plural = "Haydovchilar"
        ordering = ['-id']

    def __str__(self):
        return self.ism

    @property
    def jami_qarz(self):
        qarz = 0
        for p in self.putyovkalar.exclude(status='tugagan'):
            qarz += p.qarz
        for d in self.dazvollar.exclude(status='tugagan'):
            qarz += d.qarz
        for t in self.tirlar.exclude(status='tugagan'):
            qarz += t.qarz
        return qarz

    @property
    def jami_tolangan(self):
        from django.db.models import Sum
        s = 0
        s += self.putyovkalar.aggregate(x=Sum('tolangan'))['x'] or 0
        s += self.tirlar.aggregate(x=Sum('tolangan'))['x'] or 0
        s += self.dazvollar.aggregate(x=Sum('tolangan'))['x'] or 0
        return s

    @property
    def aktiv_hujjatlar_soni(self):
        c = 0
        c += self.putyovkalar.exclude(status='tugagan').count()
        c += self.tirlar.exclude(status='tugagan').count()
        c += self.dazvollar.exclude(status='tugagan').count()
        c += self.litsenziyalar.exclude(status='tugagan').count()
        c += self.ijara_shartnomalari.exclude(status='tugagan').count()
        return c

    @property
    def aktiv_putyovka(self):
        return self.putyovkalar.exclude(status='tugagan').first()

    @property
    def aktiv_tir(self):
        return self.tirlar.exclude(status='tugagan').filter(tugash__gte=date.today()).first()

    @property
    def aktiv_dazvol(self):
        return self.dazvollar.exclude(status='tugagan').filter(tugash__gte=date.today()).first()

    @property
    def aktiv_litsenziya(self):
        return self.litsenziyalar.exclude(status='tugagan').filter(tugash__gte=date.today()).first()

    @property
    def aktiv_ijara(self):
        return self.ijara_shartnomalari.filter(status='faol').first()


class Putyovka(models.Model):
    STATUS_CHOICES = [
        ('faol', 'Faol'),
        ('tugagan', 'Tugagan'),
        ('qarzli', 'Qarzli'),
    ]

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,
                               related_name='putyovkalar', verbose_name="Haydovchi")
    raqam = models.CharField(max_length=100, blank=True, verbose_name="Raqam (pritep)")
    shifr = models.CharField(max_length=50, blank=True, verbose_name="Shifr")
    narxi = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                verbose_name="Narxi (so'm)")
    tolangan = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                   verbose_name="To'langan (so'm)")
    muddat = models.IntegerField(default=12, verbose_name="Muddat (oy)")
    boshlanish = models.DateField(verbose_name="Boshlanish sanasi")
    tugash = models.DateField(verbose_name="Tugash sanasi")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='faol',
                              verbose_name="Status")
    izoh = models.TextField(blank=True, verbose_name="Izoh")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Putyovka"
        verbose_name_plural = "Putyovkalar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.driver.ism} — Putyovka"

    @property
    def qarz(self):
        return max(0, self.narxi - self.tolangan)

    @property
    def is_expired(self):
        return self.tugash < date.today()

    @property
    def days_remaining(self):
        delta = self.tugash - date.today()
        return max(0, delta.days)

    @property
    def progress(self):
        total = (self.tugash - self.boshlanish).days
        passed = (date.today() - self.boshlanish).days
        if total <= 0:
            return 100
        return min(100, max(0, int(passed / total * 100)))

    def save(self, *args, **kwargs):
        # 'tugagan' status admin tomonidan qo'yiladi — uni qayta yozmaymiz
        if self.status != 'tugagan':
            if self.is_expired:
                self.status = 'tugagan'
            elif self.qarz > 0:
                self.status = 'qarzli'
            else:
                self.status = 'faol'
        super().save(*args, **kwargs)


class TIR(models.Model):
    STATUS_CHOICES = [
        ('faol', 'Faol'),
        ('tugagan', 'Tugagan'),
        ('qarzli', 'Qarzli'),
    ]

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,
                               related_name='tirlar', verbose_name="Haydovchi")
    tir_raqam = models.CharField(max_length=100, verbose_name="TIR raqami")
    narxi = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                verbose_name="Narxi (so'm)")
    tolangan = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                   verbose_name="To'langan (so'm)")
    muddat = models.IntegerField(default=12, verbose_name="Muddat (oy)")
    boshlanish = models.DateField(verbose_name="Boshlanish sanasi")
    tugash = models.DateField(verbose_name="Tugash sanasi")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='faol',
                              verbose_name="Status")
    izoh = models.TextField(blank=True, verbose_name="Izoh")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "TIR"
        verbose_name_plural = "TIRlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.driver.ism} — TIR {self.tir_raqam}"

    @property
    def qarz(self):
        return max(0, self.narxi - self.tolangan)

    @property
    def is_expired(self):
        return self.tugash < date.today()

    @property
    def days_remaining(self):
        return max(0, (self.tugash - date.today()).days)

    def save(self, *args, **kwargs):
        if self.status != 'tugagan':
            if self.is_expired:
                self.status = 'tugagan'
            elif self.qarz > 0:
                self.status = 'qarzli'
            else:
                self.status = 'faol'
        super().save(*args, **kwargs)


class Dazvol(models.Model):
    STATUS_CHOICES = [
        ('faol', 'Faol'),
        ('tugagan', 'Tugagan'),
        ('qarzli', 'Qarzli'),
    ]

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,
                               related_name='dazvollar', verbose_name="Haydovchi")
    mamlakat = models.CharField(max_length=100, verbose_name="Mamlakat")
    dazvol_raqam = models.CharField(max_length=100, blank=True, verbose_name="Dazvol raqami")
    narxi = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                verbose_name="Narxi (so'm)")
    tolangan = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                   verbose_name="To'langan (so'm)")
    boshlanish = models.DateField(verbose_name="Boshlanish sanasi")
    tugash = models.DateField(verbose_name="Tugash sanasi")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='faol',
                              verbose_name="Status")
    izoh = models.TextField(blank=True, verbose_name="Izoh")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Dazvol"
        verbose_name_plural = "Dazvollar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.driver.ism} — Dazvol ({self.mamlakat})"

    @property
    def qarz(self):
        return max(0, self.narxi - self.tolangan)

    @property
    def is_expired(self):
        return self.tugash < date.today()

    @property
    def days_remaining(self):
        return max(0, (self.tugash - date.today()).days)

    def save(self, *args, **kwargs):
        if self.status != 'tugagan':
            if self.is_expired:
                self.status = 'tugagan'
            elif self.qarz > 0:
                self.status = 'qarzli'
            else:
                self.status = 'faol'
        super().save(*args, **kwargs)


class Litsenziya(models.Model):
    STATUS_CHOICES = [
        ('faol', 'Faol'),
        ('tugagan', 'Tugagan'),
    ]

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,
                               related_name='litsenziyalar', verbose_name="Haydovchi")
    litsenziya_raqam = models.CharField(max_length=100, verbose_name="Litsenziya raqami")
    narxi = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                verbose_name="Narxi (so'm)")
    tolangan = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                   verbose_name="To'langan (so'm)")
    boshlanish = models.DateField(verbose_name="Boshlanish sanasi")
    tugash = models.DateField(verbose_name="Tugash sanasi")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='faol',
                              verbose_name="Status")
    izoh = models.TextField(blank=True, verbose_name="Izoh")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Litsenziya"
        verbose_name_plural = "Litsenziyalar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.driver.ism} — Litsenziya"

    @property
    def qarz(self):
        return max(0, self.narxi - self.tolangan)

    @property
    def is_expired(self):
        return self.tugash < date.today()


class IjaraShartnoma(models.Model):
    STATUS_CHOICES = [
        ('faol', 'Faol'),
        ('tugagan', 'Tugagan'),
    ]

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,
                               related_name='ijara_shartnomalari', verbose_name="Haydovchi")
    manzil = models.CharField(max_length=300, verbose_name="Manzil")
    narxi = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                verbose_name="Narxi (so'm)")
    tolangan = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                   verbose_name="To'langan (so'm)")
    boshlanish = models.DateField(verbose_name="Boshlanish sanasi")
    tugash = models.DateField(verbose_name="Tugash sanasi")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='faol',
                              verbose_name="Status")
    izoh = models.TextField(blank=True, verbose_name="Izoh")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ijara shartnomasi"
        verbose_name_plural = "Ijara shartnomalari"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.driver.ism} — Ijara"

    @property
    def qarz(self):
        return max(0, self.narxi - self.tolangan)

    @property
    def is_expired(self):
        return self.tugash < date.today()


class Chiqim(models.Model):
    TUR_CHOICES = [
        ('xizmat', 'Xizmat xarajati'),
        ('maosh', 'Maosh'),
        ('ta_mir', "Ta'mir"),
        ('boshqa', 'Boshqa'),
    ]

    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='chiqimlar', verbose_name="Haydovchi")
    tur = models.CharField(max_length=20, choices=TUR_CHOICES, default='boshqa',
                           verbose_name="Tur")
    summa = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Summa (so'm)")
    izoh = models.TextField(blank=True, verbose_name="Izoh")
    sana = models.DateField(default=date.today, verbose_name="Sana")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Chiqim"
        verbose_name_plural = "Chiqimlar"
        ordering = ['-sana']

    def __str__(self):
        return f"{self.get_tur_display()} — {self.summa} so'm"


class TolovQayd(models.Model):
    """To'lov tarixi — har qanday hujjat uchun (= Kirim)"""
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,
                               related_name='tolovlar', verbose_name="Haydovchi")
    tur = models.CharField(max_length=20, verbose_name="Hujjat turi")  # putyovka, tir, dazvol
    summa = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Summa")
    sana = models.DateField(default=date.today, verbose_name="To'lov sanasi")
    izoh = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sana']

    def __str__(self):
        return f"{self.driver.ism} — {self.tur} — {self.summa}"
