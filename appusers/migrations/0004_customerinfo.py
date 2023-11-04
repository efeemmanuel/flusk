# Generated by Django 4.2.6 on 2023-10-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0003_advance_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]