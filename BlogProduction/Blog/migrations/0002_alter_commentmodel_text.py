# Generated by Django 3.2.12 on 2022-02-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
