# Generated by Django 3.2.4 on 2021-09-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manudetails',
            fields=[
                ('contact', models.FloatField()),
                ('dist_no', models.CharField(blank=True, max_length=30, null=True)),
                ('prof', models.FileField(blank=True, default='images/default.png', null=True, upload_to='profiles/dist/')),
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'manudetails',
                'managed': False,
            },
        ),
    ]
