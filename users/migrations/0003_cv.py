# Generated by Django 2.2.2 on 2019-07-14 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20190628_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_day', models.DateTimeField()),
                ('volunteer_work', models.CharField(max_length=350)),
                ('professional_associations', models.CharField(max_length=350)),
                ('skills', models.CharField(max_length=350)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
