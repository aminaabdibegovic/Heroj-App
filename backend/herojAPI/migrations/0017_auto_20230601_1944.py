# Generated by Django 3.1.14 on 2023-06-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herojAPI', '0016_pdffajlovi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdffajlovi',
            name='odobreno',
            field=models.BooleanField(default=False),
        ),
    ]
