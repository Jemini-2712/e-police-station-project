# Generated by Django 4.0.3 on 2022-04-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0016_rename_csatus_complaint_cstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='fir',
            name='solved_by',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]