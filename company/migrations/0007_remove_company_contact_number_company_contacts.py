# Generated by Django 5.1.4 on 2025-01-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_company_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='contact_number',
        ),
        migrations.AddField(
            model_name='company',
            name='contacts',
            field=models.TextField(blank=True, null=True),
        ),
    ]
