from pathlib import Path
import argparse
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description="Копіювання файлів з сортуванням за розширеннями.")
    parser.add_argument("--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("--dest", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()


def copy_files(src, dst):
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_files(item, dst)  # Рекурсивний виклик для піддиректорій
            else:
                extension = item.suffix[1:]  # Отримання розширення файлу
                if extension:
                    extension_dir = dst / extension
                    extension_dir.mkdir(parents=True, exist_ok=True)  # Створення піддиректорії
                    shutil.copy(item, extension_dir)
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")


def main():
    args = parse_args()
    args.dest.mkdir(parents=True, exist_ok=True)  # Створюємо директорію призначення, якщо вона не існує
    copy_files(args.source, args.dest)


if __name__ == "__main__":
    main()
