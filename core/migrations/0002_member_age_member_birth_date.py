# Generated by Django 5.2.3 on 2025-06-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
