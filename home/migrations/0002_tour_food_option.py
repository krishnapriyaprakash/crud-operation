# Generated by Django 5.1.4 on 2024-12-27 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='food_option',
            field=models.CharField(choices=[('Yes', 'Food'), ('No', 'No Food')], default='No', max_length=3),
        ),
    ]
