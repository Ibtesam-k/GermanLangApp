# Generated by Django 4.2.6 on 2023-10-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PracticeHub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='noun',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
