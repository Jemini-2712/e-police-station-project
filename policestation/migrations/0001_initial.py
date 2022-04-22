# Generated by Django 4.0.3 on 2022-04-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commissioner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=50)),
                ('stationname', models.CharField(max_length=40)),
            ],
        ),
    ]