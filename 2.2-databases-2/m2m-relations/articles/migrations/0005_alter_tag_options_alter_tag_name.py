from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_tag_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тематика', 'verbose_name_plural': 'Тема'},
        ),
        migrations.AlterField(
            model_name = 'tag',
            name = 'name',
            field = models.CharField(max_length = 50, verbose_name = 'Тег'),
        ),
    ]