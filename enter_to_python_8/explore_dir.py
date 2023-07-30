"""
    ---Task 4---
Решить задачи, которые не успели решить на семинаре.
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle:
    * Для дочерних объектов указывайте родительскую директорию.
    * Для каждого объекта укажите файл это или директория.
    * Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
всех вложенных файлов и директорий.
"""
import os
import json


def explore_directory_to_json(directory):
    def get_file_size(path):
        return os.path.getsize(path) if os.path.isfile(path) else get_directory_size(path)

    def get_directory_size(directory):
        total_size = 0
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size

    def explore_directory_recursively(directory, parent=None):
        results = []
        for root, dirs, files in os.walk(directory):
            parent_name = os.path.basename(root) if parent is None else parent
            for d in dirs:
                path = os.path.join(root, d)
                size = get_file_size(path)
                results.append({
                    'type': 'directory',
                    'name': d,
                    'path': path,
                    'parent': parent_name,
                    'size_bytes': size
                })
            for f in files:
                path = os.path.join(root, f)
                size = os.path.getsize(path)
                results.append({
                    'type': 'file',
                    'name': f,
                    'path': path,
                    'parent': parent_name,
                    'size_bytes': size
                })

        return results

    results = explore_directory_recursively(directory)

    export_directory = os.path.join(os.getcwd(), 'export')
    if not os.path.exists(export_directory):
        os.makedirs(export_directory)

    json_filepath = os.path.join(export_directory, 'results.json')
    with open(json_filepath, 'w') as json_file:
        json.dump(results, json_file, indent=4)

    return results
