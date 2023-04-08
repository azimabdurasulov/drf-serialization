# Generated by Django 4.2 on 2023-04-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]