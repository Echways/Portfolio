from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0008_populate_slugs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="slug",
            field=models.SlugField(max_length=140, unique=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(max_length=140, unique=True),
        ),
    ]

