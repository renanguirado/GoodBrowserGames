# Generated by Django 4.0.4 on 2022-05-29 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220323_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacoes',
            fields=[
                ('id', models.BigAutoField(max_length=500, primary_key=True, serialize=False)),
                ('game_id', models.BigIntegerField(max_length=500)),
                ('autor', models.CharField(max_length=30)),
                ('comentario', models.CharField(max_length=200)),
                ('nota', models.BigIntegerField(max_length=500)),
            ],
        ),
    ]
