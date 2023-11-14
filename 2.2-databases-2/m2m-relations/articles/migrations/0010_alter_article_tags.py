from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'article',
            name = 'tags',
            field = models.ManyToManyField(through = 'articles.ArticleScope', to = 'articles.tag', verbose_name = 'Тема статьи'),
        ),
    ]