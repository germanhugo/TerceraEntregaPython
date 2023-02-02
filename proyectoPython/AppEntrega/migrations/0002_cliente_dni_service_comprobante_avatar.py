# Generated by Django 4.1.4 on 2023-01-23 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppEntrega', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='dni',
            field=models.CharField(default=28671036, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='comprobante',
            field=models.IntegerField(default=1236),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]