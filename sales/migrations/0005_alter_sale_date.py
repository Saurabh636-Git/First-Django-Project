# Generated by Django 3.2.5 on 2021-07-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
