# Generated by Django 2.2.3 on 2019-08-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_auto_20190803_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feebback',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]