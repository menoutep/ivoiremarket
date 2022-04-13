# Generated by Django 3.2.12 on 2022-04-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('SELLER', 'SELLER'), ('USER', 'USER')], max_length=7),
        ),
    ]