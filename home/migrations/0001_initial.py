# Generated by Django 5.0.2 on 2024-08-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('c_no', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=14)),
                ('Email', models.CharField(max_length=50)),
                ('Enquiry', models.TextField()),
            ],
        ),
    ]
