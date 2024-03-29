# Generated by Django 3.2 on 2021-04-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210424_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(blank=True, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('role', models.CharField(blank=True, max_length=30, null=True)),
                ('fullname', models.CharField(blank=True, max_length=30, null=True)),
                ('ex_id', models.IntegerField(blank=True, null=True)),
                ('upd_time', models.DateTimeField(blank=True, null=True)),
                ('ar_get', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
