# Generated by Django 4.1.6 on 2023-02-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.CharField(choices=[('OF', 'OFFICE'), ('ST', 'STUDY'), ('IP', 'IMPORTANT')], max_length=10),
        ),
    ]