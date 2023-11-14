from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_alter_articlescope_article_alter_articlescope_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'articlescope',
            name = 'article',
            field = models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, related_name = 'scopes', to = 'articles.article'),
        ),
        migrations.AlterField(
            model_name = 'articlescope',
            name = 'tag',
            field = models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, related_name = 'scopes', to = 'articles.tag', verbose_name = 'Раздел'),
        ),
    ]