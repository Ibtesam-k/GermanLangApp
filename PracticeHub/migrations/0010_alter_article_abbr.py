# Generated by Django 4.2.6 on 2024-01-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PracticeHub', '0009_article_abbr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abbr',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
