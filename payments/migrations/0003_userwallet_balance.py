# Generated by Django 4.2.6 on 2023-10-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_remove_userwallet_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwallet',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
