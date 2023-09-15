# Generated by Django 4.2.5 on 2023-09-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(verbose_name='Task')),
                ('creater', models.TextField(verbose_name='Creater')),
                ('status', models.TextField(verbose_name='Status')),
            ],
        ),
    ]