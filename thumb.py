import re

input_filename = "input.txt"  # Здесь ваши исходные строки
output_filename = "output.txt"  # Сюда запишем результат

# Паттерн для поиска нужных частей в строке
pattern = re.compile(
    r'<img\s+src="images/([^"]+)"\s+alt="([^"]*)"\s+class="thumb"\s+data-info=([^\>]+)>'
)

output_lines = []

with open(input_filename, "r", encoding="utf-8") as f:
    for line in f:
        # Поиск по паттерну
        match = pattern.search(line)
        if match:
            filename, alt, data_info = match.groups()
            new_line = (
                f'<img src="thumbnails/{filename}" data-full="images/{filename}" '
                f'alt="{alt}" class="thumb" data-info={data_info} loading="lazy">\n'
            )
            output_lines.append(new_line)
        else:
            # Если строка не совпадает — оставляем как есть или игнорируем
            output_lines.append(line)

with open(output_filename, "w", encoding="utf-8") as f:
    f.writelines(output_lines)

print(f"Готово! Новый список сохранён в {output_filename}")
