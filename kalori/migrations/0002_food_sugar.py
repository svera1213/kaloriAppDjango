# Generated by Django 2.2.12 on 2020-05-03 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalori', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='sugar',
            field=models.FloatField(default=0),
        ),
    ]