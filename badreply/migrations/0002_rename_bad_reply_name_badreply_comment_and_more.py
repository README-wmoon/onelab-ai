# Generated by Django 5.0.2 on 2024-05-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badreply', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='badreply',
            old_name='bad_reply_name',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='badreply',
            name='target',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='badreply',
            table='bad_reply',
        ),
    ]
