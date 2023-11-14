from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_articlescope_is_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name = 'article',
            options = {'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]