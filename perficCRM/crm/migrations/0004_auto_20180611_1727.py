# Generated by Django 2.0.5 on 2018-06-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20180611_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(blank=True, null=True, to='crm.Menus'),
        ),
    ]
