# Generated by Django 3.0.5 on 2020-04-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('product_detail', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
