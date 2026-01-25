from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_alter_achievments_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Achievments',
            new_name='Achievement',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]

