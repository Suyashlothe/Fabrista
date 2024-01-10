# Generated by Django 4.2.6 on 2023-12-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('product_type', models.CharField(max_length=100)),
            ],
        ),
    ]
