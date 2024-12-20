# Generated by Django 5.1.3 on 2024-11-27 06:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blocklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Adult', 'Adult'), ('Violence', 'Violence'), ('General', 'General')], max_length=100)),
                ('blocked', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DNSLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action_taken', models.CharField(choices=[('Blocked', 'Blocked'), ('Allowed', 'Allowed')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
