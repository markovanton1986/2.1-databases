from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name = 'sensor',
            name = 'description',
            field = models.TextField(blank = True),
        ),
    ]