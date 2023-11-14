from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_tag_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name = 'tag',
            name = 'is_main',
        ),
        migrations.AlterField(
            model_name = 'article',
            name = 'tags',
            field  =models.ManyToManyField(related_name = 'articles', through = 'articles.ArticleScope', to = 'articles.tag', verbose_name = 'Тема статьи'),
        ),
        migrations.AlterField(
            model_name = 'articlescope',
            name = 'article',
            field = models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, related_name = 'scope', to = 'articles.article'),
        ),
        migrations.AlterField(
            model_name = 'articlescope',
            name = 'tag',
            field = models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, related_name = 'scope', to = 'articles.tag', verbose_name = 'Раздел'),
        ),
    ]