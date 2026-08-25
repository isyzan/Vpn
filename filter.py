import requests
import random
from datetime import datetime

print("🚀 ISYZAN VPN: загрузка готовых VLESS-конфигов...")

URL = 'https://solovyov-jenya2004.vercel.app/final_sorted/'

try:
    resp = requests.get(URL, timeout=10)
    raw = resp.text
except Exception as e:
    print(f"❌ Ошибка загрузки: {e}")
    exit(1)

# Разбиваем на строки, убираем пустые
lines = [line.strip() for line in raw.splitlines() if line.strip()]
print(f"📡 Всего серверов в источнике: {len(lines)}")

# Отбираем только VLESS-строки (которые начинаются с vless://)
vless_lines = [line for line in lines if line.startswith('vless://')]
print(f"✅ Найдено VLESS-конфигов: {len(vless_lines)}")

if not vless_lines:
    print("❌ VLESS-конфиги не найдены!")
    exit(1)

# Берём первые 100 (или меньше, если их меньше 100)
selected = vless_lines[:100]
print(f"✅ Выбрано {len(selected)} серверов")

# Перемешиваем для разнообразия
random.shuffle(selected)

# Создаём файл с шапкой
OUTPUT_FILE = 'isyzan_vpn.txt'
with open(OUTPUT_FILE, 'w') as f:
    f.write("# ISYZAN VPN 🚀\n")
    f.write("# Обход белых списков и глушилок\n")
    f.write("# Поддержка: @isyzan\n")
    f.write("# Канал: @isy_zan1\n")
    f.write(f"# Обновлено: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"# Всего серверов: {len(selected)}\n")
    f.write("\n")
    for line in selected:
        f.write(line + "\n")

print(f"🎉 Файл создан: {OUTPUT_FILE}")
print(f"📊 Всего серверов: {len(selected)}")
