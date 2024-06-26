# Generated by Django 4.2.6 on 2023-10-16 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('plural', models.CharField(max_length=75)),
                ('plural_abbr', models.CharField(max_length=50)),
                ('singular_article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PracticeHub.article')),
            ],
        ),
    ]
