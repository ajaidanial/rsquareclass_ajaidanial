# Generated by Django 3.0.2 on 2020-01-17 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batches', to='main_app.Year'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='main_app.Group'),
        ),
    ]
