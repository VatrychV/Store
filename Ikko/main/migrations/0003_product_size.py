# Generated by Django 4.1.3 on 2024-01-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_costomer_customer_alter_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='S', max_length=100),
        ),
    ]
