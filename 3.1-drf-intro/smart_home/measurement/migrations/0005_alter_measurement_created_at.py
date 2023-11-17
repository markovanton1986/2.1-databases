from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_measurement_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'measurement',
            name = 'created_at',
            field = models.DateTimeField(auto_now_add = True, null = True),
        ),
    ]