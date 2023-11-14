from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name = 'tag',
            name = 'is_main',
            field = models.ManyToManyField(related_name = 'is_main', through = 'articles.ArticleScope', to = 'articles.article'),
        ),
    ]