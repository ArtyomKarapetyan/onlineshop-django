# Generated by Django 4.0.3 on 2022-04-17 08:10

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_id_variation'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='variation',
            managers=[
                ('objetcs', django.db.models.manager.Manager()),
            ],
        ),
    ]
