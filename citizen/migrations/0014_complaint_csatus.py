# Generated by Django 4.0.3 on 2022-04-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0013_fir_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='csatus',
            field=models.BooleanField(default=True),
        ),
    ]