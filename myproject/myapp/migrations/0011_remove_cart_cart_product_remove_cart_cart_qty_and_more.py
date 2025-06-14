# Generated by Django 5.2.1 on 2025-05-24 04:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cart_qty',
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_qty', models.PositiveIntegerField(default=0)),
                ('cart_amount', models.PositiveIntegerField(default=0)),
                ('cart_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
                ('cart_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]
