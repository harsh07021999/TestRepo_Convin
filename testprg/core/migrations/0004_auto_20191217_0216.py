# Generated by Django 2.2.5 on 2019-12-16 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191217_0149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='state_check',
            new_name='state_check1',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='test_feild',
        ),
    ]
