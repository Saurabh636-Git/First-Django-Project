# Generated by Django 3.2.5 on 2021-07-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_sale_tr_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]