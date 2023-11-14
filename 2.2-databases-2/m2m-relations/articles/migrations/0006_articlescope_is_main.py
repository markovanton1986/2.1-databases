from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_tag_options_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name = 'articlescope',
            name = 'is_main',
            field = models.BooleanField(default = False, verbose_name = 'Основной'),
        ),
    ]