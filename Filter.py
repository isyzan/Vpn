import requests
import random
import sys
from datetime import datetime

print("🚀 ISYZAN VPN FILTER: генерация серверов с именами...")

URL = 'https://solovyov-jenya2004.vercel.app/final_sorted/'

try:
    resp = requests.get(URL, timeout=10)
    raw = resp.text
except Exception as e:
    print(f"❌ Ошибка загрузки: {e}")
    sys.exit(1)

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

if len(working) >= 100:
    final.extend(random.sample(working, 100))
else:
    final.extend(working)
    extra = lines[200:]
    random.shuffle(extra)
    need = 100 - len(working)
    final.extend(extra[:need])

if len(dead) >= 20:
    final.extend(random.sample(dead, 20))
else:
    final.extend(dead)
    extra_dead = lines[200:250]
    random.shuffle(extra_dead)
    final.extend(extra_dead[:20 - len(dead)])

# Перемешиваем
random.shuffle(final)

# Разделяем рабочие и нерабочие (для именования)
work_count = min(100, len(working))
dead_count = len(final) - work_count

# Собираем финальный список с именами
named_servers = []

# Рабочие серверы с именами "Обход глушилок 1..100"
for i in range(work_count):
    named_servers.append(f"Обход глушилок {i+1} = {final[i]}")

# Нерабочие (тестовые) с именами "Тест глушилки 1..20"
for j in range(dead_count):
    idx = work_count + j
    named_servers.append(f"Тест глушилки {j+1} = {final[idx]}")

# Перемешиваем ещё раз, чтобы тесты были вразброс
random.shuffle(named_servers)

# Создаём файл с шапкой и именами
OUTPUT_FILE = 'isyzan_vpn.txt'
with open(OUTPUT_FILE, 'w') as f:
    f.write("# ISYZAN VPN 🚀\n")
    f.write("# Обход белых списков и глушилок\n")
    f.write("# Поддержка: @isyzan\n")
    f.write("# Канал: @isy_zan1\n")
    f.write(f"# Обновлено: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"# Всего серверов: {len(named_servers)} (рабочие + 20 тестовых)\n")
    f.write("\n")
    for line in named_servers:
        f.write(line + "\n")

print(f"🎉 Файл создан: {OUTPUT_FILE}")
print(f"📊 Всего серверов: {len(named_servers)}")
print("✅ Первые 5 серверов:")
for line in named_servers[:5]:
    print(f"   {line}")
