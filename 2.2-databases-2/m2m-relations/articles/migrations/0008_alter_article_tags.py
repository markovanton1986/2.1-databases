from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'article',
            name = 'tags',
            field = models.ManyToManyField(related_name = 'articles', through = 'articles.ArticleScope', to = 'articles.tag', verbose_name = 'Тема статьи'),
        ),
    ]