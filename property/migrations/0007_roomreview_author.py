# Generated by Django 3.1.3 on 2020-12-23 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_remove_roombook_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomreview',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='review_author', to='auth.user'),
            preserve_default=False,
        ),
    ]
