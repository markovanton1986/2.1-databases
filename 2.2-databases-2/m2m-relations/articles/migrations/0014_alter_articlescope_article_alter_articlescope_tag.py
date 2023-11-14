from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_remove_tag_is_main_alter_article_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'articlescope',
            name = 'article',
            field = models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, related_name = 'rel_name', to = 'articles.article'),
        ),
        migrations.AlterField(
            model_name = 'articlescope',
            name = 'tag',
            field = models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, related_name = 'rel_name', to = 'articles.tag', verbose_name = 'Раздел'),
        ),
    ]