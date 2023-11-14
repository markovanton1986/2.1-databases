from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_tags_alter_articlescope_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'tag',
            name = 'name',
            field = models.CharField(max_length = 50, verbose_name = 'Тема'),
        ),
    ]