# Generated by Django 3.2.5 on 2021-07-26 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_alter_sale_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='items',
        ),
        migrations.AddField(
            model_name='sale',
            name='items',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.item'),
        ),
    ]