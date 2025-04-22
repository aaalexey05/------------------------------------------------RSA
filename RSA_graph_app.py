import tkinter as tk
from tkinter import messagebox
import math

# Функции для RSA
def is_prime(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def gcd(a, b):
    """Наибольший общий делитель"""
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    """Поиск мультипликативного обратного"""
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2 - temp1 * x1
        y = y2 - temp1 * y1
        
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    
    if temp_phi == 1:
        d = y2 + phi
    
    return d

def generate_keypair(p, q):
    """Генерация пары ключей"""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Оба числа должны быть простыми")
    
    n = p * q
    phi = (p-1) * (q-1)
    
    e = 65537  # Распространенное значение для e
    while gcd(e, phi) != 1:
        e -= 1
    
    d = multiplicative_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    """Шифрование сообщения"""
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    """Дешифрование сообщения"""
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# Функции для работы с графическим интерфейсом
def encrypt_message():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        public, private = generate_keypair(p, q)
        public_key_label.config(text=f"Публичный ключ (e, n): {public}")
        private_key_label.config(text=f"Приватный ключ (d, n): {private}")
        
        message = entry_message.get()
        encrypted_msg = encrypt(public, message)
        encrypted_msg_label.config(text=f"Зашифрованное сообщение: {encrypted_msg}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

def decrypt_message():
    try:
        d = int(entry_d.get())
        n = int(entry_n.get())
        private_key = (d, n)
        
        cipher_input = entry_ciphertext.get()
        ciphertext = list(map(int, cipher_input.split()))
        
        decrypted_msg = decrypt(private_key, ciphertext)
        decrypted_msg_label.config(text=f"Дешифрованное сообщение: {decrypted_msg}")
    except Exception as e:
        messagebox.showerror("Ошибка", "Ошибка при дешифровании. Проверьте введенные данные.")

# Создание окна Tkinter
root = tk.Tk()
root.title("RSA Шифрование/Дешифрование")

# Режим шифрования
frame_encryption = tk.LabelFrame(root, text="Шифрование", padx=10, pady=10)
frame_encryption.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame_encryption, text="Введите простое число p:").grid(row=0, column=0, sticky="e")
entry_p = tk.Entry(frame_encryption)
entry_p.grid(row=0, column=1)

tk.Label(frame_encryption, text="Введите простое число q:").grid(row=1, column=0, sticky="e")
entry_q = tk.Entry(frame_encryption)
entry_q.grid(row=1, column=1)

tk.Label(frame_encryption, text="Введите сообщение для шифрования:").grid(row=2, column=0, sticky="e")
entry_message = tk.Entry(frame_encryption, width=50)
entry_message.grid(row=2, column=1)

encrypt_button = tk.Button(frame_encryption, text="Зашифровать", command=encrypt_message)
encrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

public_key_label = tk.Label(frame_encryption, text="Публичный ключ (e, n):")
public_key_label.grid(row=4, column=0, columnspan=2)

private_key_label = tk.Label(frame_encryption, text="Приватный ключ (d, n):")
private_key_label.grid(row=5, column=0, columnspan=2)

encrypted_msg_label = tk.Label(frame_encryption, text="Зашифрованное сообщение:")
encrypted_msg_label.grid(row=6, column=0, columnspan=2)

# Режим дешифрования
frame_decryption = tk.LabelFrame(root, text="Дешифрование", padx=10, pady=10)
frame_decryption.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_decryption, text="Введите секретный ключ d:").grid(row=0, column=0, sticky="e")
entry_d = tk.Entry(frame_decryption)
entry_d.grid(row=0, column=1)

tk.Label(frame_decryption, text="Введите n:").grid(row=1, column=0, sticky="e")
entry_n = tk.Entry(frame_decryption)
entry_n.grid(row=1, column=1)

tk.Label(frame_decryption, text="Введите зашифрованное сообщение:").grid(row=2, column=0, sticky="e")
entry_ciphertext = tk.Entry(frame_decryption, width=50)
entry_ciphertext.grid(row=2, column=1)

decrypt_button = tk.Button(frame_decryption, text="Дешифровать", command=decrypt_message)
decrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

decrypted_msg_label = tk.Label(frame_decryption, text="Дешифрованное сообщение:")
decrypted_msg_label.grid(row=4, column=0, columnspan=2)


if __name__ == "__main__":
    # Запуск программы
    root.mainloop()
