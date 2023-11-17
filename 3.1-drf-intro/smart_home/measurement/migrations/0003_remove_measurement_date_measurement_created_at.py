from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_sensor_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name = 'measurement',
            name = 'date',
        ),
        migrations.AddField(
            model_name = 'measurement',
            name = 'created_at',
            field = models.DateTimeField(blank = True, null = True),
        ),
    ]