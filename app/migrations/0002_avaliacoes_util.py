# Generated by Django 4.0.4 on 2022-06-04 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacoes',
            name='util',
            field=models.BigIntegerField(default=0, max_length=500),
        ),
    ]
