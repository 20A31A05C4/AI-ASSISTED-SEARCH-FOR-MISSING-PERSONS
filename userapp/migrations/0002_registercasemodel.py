# Generated by Django 4.1.5 on 2023-01-16 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registercasemodel',
            fields=[
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('photo', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'db_table': 'register_case',
            },
        ),
    ]
