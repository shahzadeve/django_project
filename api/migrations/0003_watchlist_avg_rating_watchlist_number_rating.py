# Generated by Django 5.1.2 on 2024-11-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
