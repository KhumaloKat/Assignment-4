# Generated by Django 5.0.6 on 2024-07-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('LS', 'Lifestyle'), ('TC', 'Technology'), ('BS', 'Business'), ('SC', 'Science'), ('PC', 'Politics'), ('CR', 'Creativity')], max_length=2)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
