# Generated by Django 4.2.5 on 2023-09-17 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_rename_status_ifctask_status_ifctask_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ifctask',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
    ]