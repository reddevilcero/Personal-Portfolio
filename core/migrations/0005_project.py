# Generated by Django 2.2 on 2019-06-04 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190529_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('project_type', models.CharField(choices=[('commercial', 'commercial'), ('personal', 'personal'), ('volunteer', 'volunteer')], max_length=50, verbose_name='Type of project')),
                ('website', models.URLField(verbose_name='Website')),
                ('screenshot', models.ImageField(upload_to='img/screenshots', verbose_name='Web screenshot')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Learning', verbose_name='Technology used')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
    ]
