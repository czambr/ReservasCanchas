# Generated by Django 4.1.7 on 2023-04-15 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Reserva', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='correo',
        ),
        migrations.AddField(
            model_name='persona',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
