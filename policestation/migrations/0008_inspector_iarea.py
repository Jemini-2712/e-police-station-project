# Generated by Django 4.0.3 on 2022-04-16 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policestation', '0007_remove_inspector_iarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspector',
            name='iarea',
            field=models.CharField(default=True, max_length=50, null=True),
        ),
    ]
