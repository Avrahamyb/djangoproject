# Generated by Django 4.2.7 on 2023-11-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='description',
            field=models.TextField(default=''),
        ),
    ]