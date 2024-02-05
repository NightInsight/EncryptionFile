from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from os import urandom

def encrypt_file(input_file_path, output_file_path, key):
    # Генерация случайного вектора инициализации (IV)
    iv = urandom(16)
    # Создание шифра AES с режимом CFB
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Чтение исходного файла и его шифрование
    with open(input_file_path, 'rb') as f:
        plaintext = f.read()

    # Дополнение данных до полного блока
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    # Запись зашифрованных данных в выходной файл
    with open(output_file_path, 'wb') as f:
        f.write(iv + ciphertext)

# Заданные пути к файлам
input_file = 'C:/Users/Nikolay/Desktop/Текст.doc'
output_file = 'C:/Users/Nikolay/Desktop/encrypted.bin'
key_file_path = 'C:/Users/Nikolay/Desktop/key.txt'

# Генерация ключа
key = urandom(32)

# Сохранение ключа
with open(key_file_path, "wb") as key_file:
    key_file.write(key)

# Шифрование файла
encrypt_file(input_file, output_file, key)