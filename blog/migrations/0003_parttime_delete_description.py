# Generated by Django 4.1.6 on 2023-05-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_animal_area_description_log_zone_zookeeper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parttime',
            fields=[
                ('pt_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pt_part', models.CharField(max_length=20)),
                ('pt_start', models.DateTimeField()),
                ('pt_end', models.DateTimeField()),
            ],
            options={
                'db_table': 'parttime',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
