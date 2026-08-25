import requests
import re
from datetime import datetime

print("🚀 ISYZAN VPN: замена имён серверов...")

URL = 'https://solovyov-jenya2004.vercel.app/final_sorted/'

try:
    resp = requests.get(URL, timeout=15)
    raw = resp.text
except Exception as e:
    print(f"❌ Ошибка загрузки: {e}")
    exit(1)

lines = [line.strip() for line in raw.splitlines() if line.strip()]
print(f"📡 Всего строк: {len(lines)}")

vless_lines = []
for line in lines:
    if line.startswith('vless://'):
        # Убираем старые имена (всё после #)
        clean_line = line.split('#')[0].strip()
        if '@' in clean_line:
            vless_lines.append(clean_line)

print(f"✅ Отобрано чистых VLESS: {len(vless_lines)}")

if not vless_lines:
    print("❌ Не найдено VLESS-ссылок!")
    with open('isyzan_vpn.txt', 'w') as f:
        f.write("# ISYZAN VPN 🚀\n# Ошибка: не найдены конфиги\n")
    exit(0)

# Берём 100 штук и переименовываем
selected = vless_lines[:100]
renamed = []
for i, link in enumerate(selected):
    # Добавляем новое имя после #
    renamed.append(f"{link}#Обход_глушилок_{i+1}")

OUTPUT_FILE = 'isyzan_vpn.txt'
with open(OUTPUT_FILE, 'w') as f:
    f.write("# ISYZAN VPN 🚀\n")
    f.write("# Обход белых списков и глушилок\n")
    f.write("# Поддержка: @isyzan\n")
    f.write("# Канал: @isy_zan1\n")
    f.write(f"# Обновлено: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"# Всего серверов: {len(renamed)}\n")
    f.write("\n")
    for line in renamed:
        f.write(line + "\n")

print(f"🎉 Файл создан: {OUTPUT_FILE}")
print(f"📊 Всего серверов: {len(renamed)}")
print("✅ Первые 3 сервера:")
for link in renamed[:3]:
    name = link.split('#')[-1]
    print(f"   {name}")
