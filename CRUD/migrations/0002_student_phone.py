# Generated by Django 4.1.7 on 2023-03-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]