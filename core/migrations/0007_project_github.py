# Generated by Django 2.2 on 2019-06-16 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190606_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gitHub',
            field=models.URLField(null=True, verbose_name='GitHub link'),
        ),
    ]