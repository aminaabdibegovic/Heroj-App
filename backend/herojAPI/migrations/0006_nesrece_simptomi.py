# Generated by Django 4.2.1 on 2023-05-18 12:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('herojAPI', '0005_remove_nesrece_korisnikid'),
    ]

    operations = [
        migrations.AddField(
            model_name='nesrece',
            name='simptomi',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
