import zipfile


def extract_zip(file_path, extract_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)


# Exemplo de uso
zip_file = input('Digite o caminho do arquivo zip: ')
extract_directory = 'C:\\Users\\ModalGR\\Desktop'

extract_zip(zip_file, extract_directory)

exit()