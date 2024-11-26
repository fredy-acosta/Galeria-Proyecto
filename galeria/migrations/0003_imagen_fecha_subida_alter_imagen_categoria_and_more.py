# Generated by Django 5.1.3 on 2024-11-18 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_remove_imagen_fecha_subida_imagen_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='fecha_subida',
            field=models.DateTimeField(auto_now_add=True, default='camara'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagen',
            name='categoria',
            field=models.CharField(choices=[('camara', 'Cámara'), ('capturas', 'Capturas de pantalla'), ('whatsapp', 'WhatsApp'), ('descargas', 'Descargas'), ('instagram', 'Instagram'), ('facebook', 'Facebook'), ('telegram', 'Telegram'), ('mms', 'Mensajes (MMS)'), ('editadas', 'Editadas'), ('snapchat', 'Snapchat'), ('tiktok', 'TikTok'), ('videos', 'Videos'), ('panoramicas', 'Panorámicas'), ('selfies', 'Selfies'), ('fondos', 'Fondos de pantalla'), ('documentos', 'Documentos'), ('gifs', 'GIFs'), ('otros', 'Otros')], default='otros', max_length=20),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
