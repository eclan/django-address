# Generated by Django 2.0 on 2017-12-09 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0010_auto_20171209_1642'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locality',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='locality',
            name='postal_code',
        ),
    ]
