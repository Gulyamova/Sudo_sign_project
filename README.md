# База дорожных знаков: Python-C++ интерфейс

## Требования

Перед началом убедитесь, что у вас установлены следующие инструменты:

- C++17 или выше
- Python 3.x
- `Conan` для управления зависимостями
- `CMake` для сборки проекта

### Установка зависимостей

Убедитесь, что у вас установлен `Conan`. Если нет, его можно установить через `pip`:

```bash
pip install conan
```

## Структура проекта

```plaintext
<project_root>
│
├── src/                    
│   ├── sign.h                
│   ├── bindings.cpp         
│
├── tests/                    
│   └── tests.py             
│
├── CMakeLists.txt            
├── conanfile.txt             
└── README.md                  
```

## Сборка и установка

1. Клонируйте репозиторий и перейдите в директорию проекта:

   ```bash
   git clone <repository-url>
   cd road_sign_project
   ```

2. Установите зависимости через Conan:

   ```bash
   conan install . --build=missing
   ```

3. Создайте директорию `build` и выполните сборку проекта с помощью `CMake`:

   ```bash
   mkdir build
   cd build
   cmake ..
   make
   ```

4. После успешной сборки в директории `build/` появится скомпилированная библиотека `sign_module.so`.

## Запуск тестов

Для тестирования проекта используйте скрипт `tests.py`, расположенный в директории `tests`:
```
python3 tests/tests.py
```

## Использование проекта

Чтобы использовать проект, создайте Python-скрипт, который импортирует и взаимодействует с модулем `sign_module`. Вот пример:

1. Создайте файл Python (например, `test.py`) в директории `build`:

```python
import sys
import os

sys.path.append(os.path.dirname(__file__))

import sign_module

db = sign_module.SignDatabase()
sign1 = sign_module.Sign("Stop", 1, sign_module.Coordinates(27.1012, 24.2412))
db.add_sign(sign1)

found_sign = db.find_sign(1)
print(f"Найден знак: {found_sign.name}, ID: {found_sign.id}, Координаты: ({found_sign.coordinates.longitude}, {found_sign.coordinates.latitude})")
```

2. Запустите скрипт:

   ```bash
   python3 tests.py
   ```

Вывод должен показать, что знак был добавлен и успешно найден:

```plaintext
Найден знак: Stop, ID: 1, Координаты: (27.1012, 24.2412)
```

