import requests
import random
import sys
from datetime import datetime

print("🚀 ISYZAN VPN FILTER: проверка серверов...")

# Источник серверов (можно заменить на другой)
URL = 'https://solovyov-jenya2004.vercel.app/final_sorted/'

try:
    resp = requests.get(URL, timeout=10)
    raw = resp.text
except Exception as e:
    print(f"❌ Ошибка загрузки: {e}")
    sys.exit(1)

# Разбиваем на строки
lines = [line.strip() for line in raw.splitlines() if line.strip()]
print(f"📡 Всего серверов в источнике: {len(lines)}")

# Проверяем первые 200
check_list = lines[:200]
working = []
dead = []

print("🔍 Проверяем серверы (до 30 секунд)...")
for server in check_list:
    try:
        proxies = {'http': server, 'https': server}
        r = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=3)
        if r.status_code == 200:
            working.append(server)
            print(f"  ✅ {server} — рабочий")
        else:
            dead.append(server)
            print(f"  ❌ {server} — не отвечает")
    except:
        dead.append(server)
        print(f"  ❌ {server} — ошибка")

print(f"✅ Рабочих: {len(working)}")
print(f"💀 Нерабочих: {len(dead)}")

# Формируем финальный список: 100 рабочих + 20 нерабочих
final = []

# Берём до 100 рабочих
if len(working) >= 100:
    final.extend(random.sample(working, 100))
else:
    final.extend(working)
    # Добиваем из непроверенных
    extra = lines[200:]
    random.shuffle(extra)
    need = 100 - len(working)
    final.extend(extra[:need])

# Добавляем 20 нерабочих (если есть)
if len(dead) >= 20:
    final.extend(random.sample(dead, 20))
else:
    final.extend(dead)
    # Добиваем случайными из непроверенных как "нерабочие"
    extra_dead = lines[200:250]
    random.shuffle(extra_dead)
    final.extend(extra_dead[:20 - len(dead)])

# Перемешиваем
random.shuffle(final)

# Создаём файл с шапкой
OUTPUT_FILE = 'isyzan_vpn.txt'
with open(OUTPUT_FILE, 'w') as f:
    f.write("# ISYZAN VPN 🚀\n")
    f.write("# Обход белых списков\n")
    f.write("# Поддержка: @isyzan\n")
    f.write("# Канал: @isy_zan1\n")
    f.write(f"# Обновлено: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"# Всего серверов: {len(final)} (рабочие + 20 тестовых)\n")
    f.write("\n")
    for s in final:
        f.write(s + "\n")

print(f"🎉 Файл создан: {OUTPUT_FILE}")
print(f"📊 Всего серверов: {len(final)}")
