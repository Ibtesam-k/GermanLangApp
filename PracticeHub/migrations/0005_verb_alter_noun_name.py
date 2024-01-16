# Generated by Django 4.2.6 on 2023-10-25 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PracticeHub', '0004_noun_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=100, unique=True)),
                ('akk', models.BooleanField()),
                ('note', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='noun',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
