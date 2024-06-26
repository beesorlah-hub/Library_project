# Generated by Django 5.0.6 on 2024-05-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=100)),
                ('book', models.CharField(max_length=100)),
                ('borrower', models.CharField(max_length=100)),
                ('loan', models.DateField(max_length=100)),
            ],
        ),
    ]
