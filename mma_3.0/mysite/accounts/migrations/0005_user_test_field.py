# Generated by Django 2.0.4 on 2018-04-19 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_test_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test_field',
            field=models.CharField(default='Hi', max_length=2),
        ),
    ]
