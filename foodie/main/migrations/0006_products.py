# Generated by Django 3.1.6 on 2021-07-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0005_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('dis', models.CharField(max_length=10)),
                ('img', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
