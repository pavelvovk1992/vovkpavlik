# Generated by Django 3.2.8 on 2021-12-14 16:48

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_seller_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=main.models.get_random_code, max_length=4)),
                ('confirmed', models.BooleanField(null=True, verbose_name='Номер подтвержден')),
                ('response', models.TextField()),
                ('seller', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.seller')),
            ],
        ),
    ]