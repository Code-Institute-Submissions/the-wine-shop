# Generated by Django 3.1.2 on 2020-11-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20201030_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_shoppingbag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]