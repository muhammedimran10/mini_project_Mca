# Generated by Django 4.2 on 2023-04-10 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0006_alter_application_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('cr_at', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversitionmessages', to='jobs.application')),
                ('cr_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversitionmessages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['cr_at'],
            },
        ),
    ]
