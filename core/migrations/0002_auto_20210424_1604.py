# Generated by Django 3.2 on 2021-04-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight_types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Weight_types',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='QodexUser',
        ),
    ]
