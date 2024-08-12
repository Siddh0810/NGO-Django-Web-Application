# Generated by Django 4.2.6 on 2023-10-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Mobile', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=250)),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
