# Generated by Django 4.2.6 on 2023-10-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='beginners_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videofile', models.FileField(null=True, upload_to='beginners_video', verbose_name='')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=60)),
                ('minutes', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
