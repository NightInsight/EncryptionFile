from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def decrypt_file(input_file_path, output_file_path, key):
    # Чтение зашифрованных данных из файла
    with open(input_file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    # Создание шифра AES с режимом CFB для расшифровки
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Удаление дополнения из расшифрованных данных
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    # Запись расшифрованных данных в выходной файл
    with open(output_file_path, 'wb') as f:
        f.write(decrypted_data)

# Заданные пути к файлам
input_file = 'C:/Users/Nikolay/Desktop/encrypted.bin'
output_file = 'C:/Users/Nikolay/Desktop/Расшифровка.doc'
key_file_path = 'C:/Users/Nikolay/Desktop/key.txt'

# Чтение ключа
with open(key_file_path, "rb") as key_file:
    key = key_file.read()

# Расшифровка файла
decrypt_file(input_file, output_file, key)