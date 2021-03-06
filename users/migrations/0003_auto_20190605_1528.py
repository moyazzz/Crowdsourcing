# Generated by Django 2.1.7 on 2019-06-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_random_rounds_testing'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RoundsNum',
        ),
        migrations.AlterModelOptions(
            name='imagemodel',
            options={'ordering': ('img',)},
        ),
        migrations.AlterField(
            model_name='attribute',
            name='word',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='imageID',
            field=models.CharField(default='Caltech101/airplanes/image_0001.jpg', max_length=64),
        ),
    ]
