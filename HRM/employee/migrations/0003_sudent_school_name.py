# Generated by Django 3.1.3 on 2020-12-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_sudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudent',
            name='school_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
