# Generated by Django 3.0.3 on 2020-05-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_products_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
