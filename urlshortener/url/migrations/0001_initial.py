# Generated by Django 5.1.1 on 2024-10-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=10, unique=True)),
                ('url', models.URLField()),
                ('visits', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
