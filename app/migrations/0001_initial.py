# Generated by Django 4.2.7 on 2024-02-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('cprincipal', models.CharField(max_length=100)),
                ('cloc', models.CharField(max_length=100)),
            ],
        ),
    ]
