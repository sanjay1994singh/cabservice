# Generated by Django 3.2.23 on 2024-02-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100, null=True)),
                ('video_link', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
