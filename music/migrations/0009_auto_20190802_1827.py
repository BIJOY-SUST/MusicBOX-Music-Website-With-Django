# Generated by Django 2.2.3 on 2019-08-02 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20190802_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='user_id',
            new_name='user',
        ),
    ]
