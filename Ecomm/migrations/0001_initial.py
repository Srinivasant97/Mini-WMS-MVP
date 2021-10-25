# Generated by Django 3.2.3 on 2021-10-23 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_number', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
                ('quantity', models.IntegerField()),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecomm.order')),
            ],
        ),
    ]