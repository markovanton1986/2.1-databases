from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_remove_measurement_date_measurement_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'measurement',
            name = 'created_at',
            field = models.DateTimeField(auto_now = True, null = True),
        ),
        migrations.AlterField(
            model_name = 'measurement',
            name = 'sensor_id',
            field = models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, related_name = 'measurements', to = 'measurement.sensor'),
        ),
    ]