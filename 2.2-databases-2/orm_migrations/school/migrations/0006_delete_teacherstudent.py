from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_student_teachers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeacherStudent',
        ),
    ]