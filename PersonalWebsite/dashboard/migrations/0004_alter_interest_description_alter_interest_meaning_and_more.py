# Generated by Django 5.1.3 on 2024-11-16 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_interest_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='meaning',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='quote',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='why_chose',
            field=models.TextField(blank=True, null=True),
        ),
    ]
