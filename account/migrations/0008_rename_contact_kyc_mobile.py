# Generated by Django 4.2.6 on 2023-10-15 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_kyc_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kyc',
            old_name='contact',
            new_name='mobile',
        ),
    ]
