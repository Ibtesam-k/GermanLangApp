# Generated by Django 4.2.6 on 2023-12-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PracticeHub', '0006_verb_meaning'),
    ]

    operations = [
        migrations.AddField(
            model_name='verb',
            name='perfect_form',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='verb',
            name='perfect_verb',
            field=models.CharField(max_length=10, null=True),
        ),
    ]