from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_tag_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'tag',
            name = 'is_main',
            field = models.ManyToManyField(through = 'articles.ArticleScope', to = 'articles.article'),
        ),
    ]