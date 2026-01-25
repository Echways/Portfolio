from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0006_teammember"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="slug",
            field=models.SlugField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name="project",
            name="slug",
            field=models.SlugField(blank=True, max_length=140),
        ),
    ]

