# Generated by Django 3.2 on 2021-04-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ol_id', models.CharField(blank=True, max_length=15, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('cover', models.ImageField(upload_to='media/cover_pics/')),
                ('desc', models.TextField(blank=True)),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
