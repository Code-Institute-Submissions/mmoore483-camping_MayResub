# Generated by Django 3.2 on 2022-05-16 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='customer_id',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.PROTECT, to='booking.newuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Cancelled'), ('A', 'Approved')], default='P', max_length=2),
        ),
    ]
