from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_scope_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'article',
            name = 'tags',
            field = models.ManyToManyField(through = 'articles.ArticleScope', to = 'articles.tag', verbose_name = 'Тема статьи'),
        ),
        migrations.AlterField(
            model_name = 'articlescope',
            name = 'tag',
            field = models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, to = 'articles.tag', verbose_name = 'Раздел'),
        ),
    ]