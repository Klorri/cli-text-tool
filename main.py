import argparse
import os
import re
import shutil
import yaml # type: ignore

def search_and_replace(file_path, search_text, replace_text, use_regex=False, backup=False):
    """Функция для замены текста в файле."""
    try:
        if backup:
            backup_path = f"{file_path}.bak"
            shutil.copy(file_path, backup_path)
            print(f"Backup created: {backup_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Содержимое файла до замены:")
            print(content)

        if use_regex:
            new_content = re.sub(search_text, replace_text, content)
        else:
            new_content = content.replace(search_text, replace_text)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"Заменено '{search_text}' на '{replace_text}' в файле '{file_path}'.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def process_directory(directory_path, search_text, replace_text, use_regex=False, backup=False):
    """Функция для обработки директорий."""
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            search_and_replace(file_path, search_text, replace_text, use_regex, backup)

def main():
    parser = argparse.ArgumentParser(description="Поиск и замена текста в файлах с поддержкой regex и резервных копий.")
    parser.add_argument("path", help="Путь к файлу или директории")
    parser.add_argument("search_text", help="Текст или регулярное выражение для поиска")
    parser.add_argument("replace_text", help="Текст для замены")
    parser.add_argument("--regex", action="store_true", help="Использовать regex для поиска")
    parser.add_argument("--backup", action="store_true", help="Создать резервную копию перед изменением файлов")
    parser.add_argument("--config", help="Путь к конфигурационному файлу (YAML)")

    args = parser.parse_args()

    if args.config:
        with open(args.config, 'r') as config_file:
            config = yaml.safe_load(config_file)
            path = config['path']
            search_text = config['search_text']
            replace_text = config['replace_text']
            use_regex = config.get('regex', False)
            backup = config.get('backup', False)
    else:
        path = args.path
        search_text = args.search_text
        replace_text = args.replace_text
        use_regex = args.regex
        backup = args.backup

    if os.path.isdir(path):
        process_directory(path, search_text, replace_text, use_regex, backup)
    else:
        search_and_replace(path, search_text, replace_text, use_regex, backup)

if __name__ == "__main__":
    main()

print("Содержимое файла до замены:Это старый текст. Он будет заменен на новый текст.Старый текст можно заменить на новый текст.")
print(content)

import argparse

def search_and_replace(file_path, search_text, replace_text, use_regex=False, backup=False):
    """Функция для замены текста в файле."""
    try:
        if backup:
            backup_path = f"{file_path}.bak"
            shutil.copy(file_path, backup_path)
            print(f"Backup created: {backup_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Содержимое файла до замены:")
            print(content)  # Выводим содержимое файла перед заменой

        if use_regex:
            new_content = re.sub(search_text, replace_text, content, flags=re.IGNORECASE)
        else:
            new_content = content.replace(search_text, replace_text)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"Заменено '{search_text}' на '{replace_text}' в файле '{file_path}'.")
        print("Содержимое файла после замены:")
        print(new_content)  # Выводим содержимое файла после замены
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Замена текста в файле.')
    parser.add_argument('path', type=str, help='Путь к файлу')
    parser.add_argument('search_text', type=str, help='Текст для поиска')
    parser.add_argument('replace_text', type=str, help='Текст для замены')
    args = parser.parse_args()

    replace_text(args.path, args.search_text, args.replace_text)