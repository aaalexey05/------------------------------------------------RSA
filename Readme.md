# RSA Шифрование

## Описание алгоритма

### На русском языке

Алгоритм RSA (Rivest–Shamir–Adleman) — это алгоритм асимметричного шифрования, который используется для защиты данных и обеспечения их безопасности при передаче. Этот алгоритм был разработан Рональдом Ривестом, Ади Шамиром и Леонардом Адлеманом в 1977 году и является одним из наиболее распространенных методов для шифрования данных, цифровых подписей и аутентификации в современных системах.

#### Принцип работы:
RSA использует пару ключей для работы с данными: **открытый ключ** и **закрытый ключ**. Это делает его асимметричным шифрованием, в отличие от симметричных алгоритмов, таких как AES, где используется один и тот же ключ для шифрования и дешифрования.

- **Открытый ключ** (public key) используется для шифрования данных. Этот ключ может быть публичным, его можно передавать любому желающему.
- **Закрытый ключ** (private key) используется для дешифрования данных и должен храниться в секрете, только у владельца.

#### Математическая основа:
Алгоритм RSA основан на свойстве больших чисел, которое сложно разложить на простые множители. Именно эта трудность является основой безопасности алгоритма. Ключи генерируются на основе двух больших простых чисел \( p \) и \( q \), и их произведение \( n \), которое используется для создания как публичного, так и приватного ключа.

#### Процесс генерации ключей:
1. Выбираются два больших простых числа \( p \) и \( q \).
2. Вычисляется их произведение \( n = p \times q \), которое используется в качестве модуля для публичного и приватного ключей.
3. Вычисляется значение функции Эйлера для числа \( n \): \( \varphi(n) = (p - 1) \times (q - 1) \).
4. Выбирается публичный ключ \( e \), который должен быть взаимно прост с \( \varphi(n) \).
5. Вычисляется закрытый ключ \( d \), который является мультипликативной обратной величиной для \( e \) по модулю \( \varphi(n) \).

#### Шифрование и дешифрование:
- **Шифрование**: Чтобы зашифровать сообщение, открытый ключ используется для возведения каждого символа в степень \( e \) по модулю \( n \).
- **Дешифрование**: Чтобы расшифровать сообщение, закрытый ключ используется для возведения зашифрованного текста в степень \( d \) по модулю \( n \).

#### Применение:
RSA широко используется для:
- **Шифрования данных**: например, в защищенных каналах связи (HTTPS, SSL/TLS).
- **Цифровых подписей**: для аутентификации и проверки целостности данных.
- **Защищенной передачи ключей**: в гибридных системах, где RSA используется для безопасного обмена симметричными ключами.

#### Преимущества RSA:
- **Высокая степень безопасности**: За счет сложности задачи разложения больших чисел на простые множители.
- **Поддержка цифровых подписей**: Позволяет убедиться в подлинности данных и их источнике.
- **Широкое применение**: Применяется в разных криптографических протоколах (например, SSL/TLS, PGP).

#### Недостатки RSA:
- **Медленная работа**: RSA требует большого вычислительного ресурса, особенно при больших ключах.
- **Размер ключей**: Для обеспечения безопасности необходимо использовать очень большие ключи (например, 2048 или 4096 бит).
- **Уязвимость к квантовым вычислениям**: В будущем, когда появятся квантовые компьютеры, алгоритм RSA может быть уязвим для атак.

### In English

The RSA algorithm (Rivest–Shamir–Adleman) is an asymmetric encryption algorithm used to protect data and ensure its security during transmission. This algorithm was developed by Ronald Rivest, Adi Shamir, and Leonard Adleman in 1977 and has become one of the most widely used methods for data encryption, digital signatures, and authentication in modern systems.

#### How It Works:
RSA uses a pair of keys for processing data: a **public key** and a **private key**. This makes it an asymmetric encryption method, unlike symmetric algorithms like AES, where the same key is used for both encryption and decryption.

- The **public key** is used for encrypting data. This key can be public and shared with anyone.
- The **private key** is used for decrypting data and must be kept secret by the owner.

#### Mathematical Foundation:
The RSA algorithm is based on the difficulty of factorizing large numbers. This difficulty forms the foundation of its security. The keys are generated based on two large prime numbers \( p \) and \( q \), and their product \( n \), which is used for both the public and private keys.

#### Key Generation Process:
1. Two large prime numbers \( p \) and \( q \) are selected.
2. Their product \( n = p \times q \) is computed, which is used as the modulus for both the public and private keys.
3. The Euler's totient function for \( n \) is computed: \( \varphi(n) = (p - 1) \times (q - 1) \).
4. A public key \( e \) is chosen such that \( e \) is coprime with \( \varphi(n) \).
5. A private key \( d \) is computed as the multiplicative inverse of \( e \) modulo \( \varphi(n) \).

#### Encryption and Decryption:
- **Encryption**: To encrypt a message, the public key is used to raise each character to the power of \( e \) modulo \( n \).
- **Decryption**: To decrypt the message, the private key is used to raise the ciphertext to the power of \( d \) modulo \( n \).

#### Applications:
RSA is widely used for:
- **Data encryption**: such as in secure communication channels (HTTPS, SSL/TLS).
- **Digital signatures**: for authentication and integrity verification of data.
- **Secure key exchange**: in hybrid systems where RSA is used for safely exchanging symmetric keys.

#### Advantages of RSA:
- **High security**: Due to the difficulty of factoring large numbers.
- **Support for digital signatures**: Allows verification of data authenticity and source.
- **Wide usage**: Used in various cryptographic protocols (e.g., SSL/TLS, PGP).

#### Disadvantages of RSA:
- **Slow operation**: RSA is computationally intensive, especially with large keys.
- **Large key sizes**: To ensure security, very large keys (e.g., 2048 or 4096 bits) must be used.
- **Vulnerability to quantum computing**: In the future, with the advent of quantum computers, RSA may become vulnerable to attacks.

---

(Описание алгоритма см. в разделе выше)

---

## Установка и зависимости

Для работы с проектом необходимо установить несколько зависимостей, которые можно установить через `pip`:

### Шаги установки:

1. **Клонирование репозитория**:
   Клонируйте репозиторий на ваш локальный компьютер с помощью команды:
   - ```bash git clone https://github.com/your-username/rsa-encryption.git```
   - ```bash cd rsa-encryption```
   - ```bash pip install -r requirements.txt```

### Как работать с проектом:
Проект включает два основных компонента: командную версию и графическое приложение.

1. **Командная версия (RSA_Crypt.py)**:
Этот файл реализует алгоритм RSA и поддерживает функции для шифрования и дешифрования текста с использованием ключей. Он работает в командной строке.

Чтобы запустить командную версию:
```bash python RSA_Crypt.py```
При запуске, программа предложит выбрать режим:

- **Шифрование**: Нужно ввести два простых числа p и 𝑞, после чего будет сгенерирован публичный и приватный ключ, и текст будет зашифрован.
- **Дешифрование**: Введите ваш закрытый ключ d и 𝑛, а также зашифрованное сообщение, чтобы расшифровать его.

2. **Графическое приложение (RSA_graph_app.py)**:
Это графическая версия, использующая библиотеку Tkinter для создания удобного интерфейса. Она позволяет пользователю вводить данные и видеть результаты шифрования и дешифрования в окне приложения.

Чтобы запустить графическое приложение:

```bash python RSA_graph_app.py```
Программа откроет окно, в котором можно будет:

- Ввести два простых числа p и q, сгенерировать публичный и приватный ключи.
- Ввести текст для шифрования и получить зашифрованное сообщение.
- Ввести закрытый ключ для дешифрования и получить расшифрованное сообщение.
