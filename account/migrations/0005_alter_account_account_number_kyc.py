# Generated by Django 4.2.6 on 2023-10-14 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0004_alter_account_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=10, max_length=11, prefix='2', unique=True),
        ),
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='kyc')),
                ('nationality', models.CharField(choices=[('india', 'India'), ('nigeria', 'Nigeria'), ('united_kingdom', 'United kingdom')], max_length=100)),
                ('marital_status', models.CharField(choices=[('married', 'Married'), ('single', 'Single'), ('other', 'Other')], max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=100)),
                ('identity_type', models.CharField(choices=[('national_id_card', 'National ID Card'), ('drivers_licence', "Driver's Licence"), ('international_passport', 'International Password'), ('other', 'Other')], max_length=140)),
                ('date_of_birth', models.DateTimeField()),
                ('signature', models.ImageField(upload_to='kyc')),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('house_address', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
