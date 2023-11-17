from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_alter_measurement_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'measurement',
            name = 'sensor_id',
            field = models.ForeignKey(null = True, on_delete = django.db.models.deletion.CASCADE, related_name = 'measurements', to = 'measurement.sensor'),
        ),
    ]