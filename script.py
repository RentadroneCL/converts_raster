import os
import subprocess
import argparse


def process_images(input_dir, output_dir=None, **kwargs):
    if output_dir is None:
        output_dir = os.getcwd()

    tif_files = [f for f in os.listdir(input_dir) if f.endswith('.tif')]
    if not tif_files:
        print("No se encontraron archivos TIFF en el directorio de entrada.")
        return

    for tif_file in tif_files:
        input_path = os.path.join(input_dir, tif_file)
        output_path = os.path.join(output_dir, tif_file)

        # Construir el comando gdal_translate con las opciones proporcionadas
        command = ['gdal_translate', input_path, output_path]
        for key, value in kwargs.items():
            command.extend(['-{} {}'.format(key, value)])

        # Ejecutar el comando gdal_translate
        try:
            subprocess.run(command, check=True)
            print("Archivo {} procesado con éxito.".format(tif_file))
        except subprocess.CalledProcessError as e:
            print("Error al procesar el archivo {}: {}".format(tif_file, e))


if __name__ == '__main__':
    # Configurar el parser de argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description='Procesar imágenes TIFF utilizando gdal_translate')
    parser.add_argument('input_dir', help='Directorio de entrada que contiene las imágenes TIFF')
    parser.add_argument('--output_dir', help='Directorio de salida para los archivos procesados')
    parser.add_argument('--option', '-o', nargs='*', help='Opciones adicionales para gdal_translate')

    args = parser.parse_args()

    # Convertir las opciones proporcionadas en un diccionario
    options = {}
    if args.option:
        for opt in args.option:
            key, value = opt.split('=')
            options[key] = value

    # Procesar las imágenes utilizando los argumentos proporcionados
    process_images(args.input_dir, args.output_dir, **options)
