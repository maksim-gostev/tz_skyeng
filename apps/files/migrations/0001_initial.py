# Generated by Django 4.2.4 on 2023-08-20 14:36

import django.core.validators
from django.db import migrations, models
import files.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeFile',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=files.models.file_handler, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['py'])])),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
