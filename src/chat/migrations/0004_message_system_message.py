# Generated by Django 3.2.15 on 2022-10-03 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chat_admins'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='system_message',
            field=models.BooleanField(default=False),
        ),
    ]