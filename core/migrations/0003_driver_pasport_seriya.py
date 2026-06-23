from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_driver_telefon'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='pasport_seriya',
            field=models.CharField(blank=True, max_length=50, verbose_name='Pasport seriya raqami'),
        ),
    ]
