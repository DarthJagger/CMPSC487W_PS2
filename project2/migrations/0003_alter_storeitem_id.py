# Generated by Django 4.2.6 on 2023-10-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0002_rename_storeitems_storeitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
