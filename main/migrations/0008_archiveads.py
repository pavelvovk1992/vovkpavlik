# Generated by Django 3.2.8 on 2021-10-27 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211026_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveAds',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.ad',),
        ),
    ]
