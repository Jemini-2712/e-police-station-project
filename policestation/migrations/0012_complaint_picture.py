# Generated by Django 4.0.3 on 2022-04-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policestation', '0011_fir_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='photo'),
        ),
    ]