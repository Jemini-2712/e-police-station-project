# Generated by Django 4.0.3 on 2022-04-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0003_fir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fir',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
