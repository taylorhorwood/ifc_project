# Generated by Django 4.2.5 on 2023-09-18 04:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_ifctask_objecttype_ifcrelsequence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ifcrelsequence',
            name='id',
        ),
        migrations.AddField(
            model_name='ifcrelsequence',
            name='GlobalId',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ifctask',
            name='GlobalId',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
