# Generated by Django 4.0.4 on 2022-04-21 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0001_initial'),
        ('actors', '0001_initial'),
        ('shows', '0006_show_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='creators.creator'),
        ),
        migrations.AlterField(
            model_name='show',
            name='star',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actors.actor'),
        ),
    ]