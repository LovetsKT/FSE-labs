import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def load_users_data():
    try:
        users_tree = ET.parse('users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
                'user_id': int(user_elem.find('user_id').text),
                'name': user_elem.find('name').text,
                'age': int(user_elem.find('age').text),
                'weight': int(user_elem.find('weight').text),
                'fitness_level': user_elem.find('fitness_level').text,
                'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл users.xml не найден")
        return []


def load_workouts_data():
    try:
        workouts_tree = ET.parse('workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'user_id': int(workout_elem.find('user_id').text),
                'date': workout_elem.find('date').text,
                'type': workout_elem.find('type').text,
                'duration': int(workout_elem.find('duration').text),
                'distance': float(workout_elem.find('distance').text),
                'calories': int(workout_elem.find('calories').text),
                'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
                'intensity': workout_elem.find('intensity').text
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл workouts.xml не найден")
        return []


def get_stats(users, workouts):
    total_workouts = len(workouts)
    total_users = len(users)
    total_calories = sum(w['calories'] for w in workouts)
    total_time = sum(w['duration'] for w in workouts) / 60
    total_distance = sum(w['distance'] for w in workouts)

    print("\n" + "=" * 50)
    print("ОБЩАЯ СТАТИСТИКА:")
    print("=" * 50)
    print(f"Всего тренировок: {total_workouts}")
    print(f"Всего пользователей: {total_users}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")
    print("=" * 50)

    return {
        'total_workouts': total_workouts,
        'total_users': total_users,
        'total_calories': total_calories,
        'total_time': total_time,
        'total_distance': total_distance
    }


def analyze_user_activity(users, workouts):
    user_stats = {}

    for user in users:
        user_workouts = [w for w in workouts if w['user_id'] == user['user_id']]
        if user_workouts:
            total_workouts = len(user_workouts)
            total_calories = sum(w['calories'] for w in user_workouts)
            total_time = sum(w['duration'] for w in user_workouts) / 60

            user_stats[user['name']] = {
                'fitness_level': user['fitness_level'],
                'total_workouts': total_workouts,
                'total_calories': total_calories,
                'total_time': total_time,
                'user': user
            }

    sorted_users = sorted(user_stats.items(), key=lambda x: x[1]['total_workouts'], reverse=True)

    print("\n" + "=" * 50)
    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    print("=" * 50)

    top_users = []
    for i, (name, stats) in enumerate(sorted_users[:3], 1):
        print(f"{i}. {name} ({stats['fitness_level']}):")
        print(f"   Тренировок: {stats['total_workouts']}")
        print(f"   Калорий: {stats['total_calories']}")
        print(f"   Время: {stats['total_time']:.1f} часов")
        top_users.append((name, stats))

    return user_stats, top_users


def analyze_workout_types(workouts):
    type_stats = {}

    for workout in workouts:
        workout_type = workout['type']
        if workout_type not in type_stats:
            type_stats[workout_type] = {
                'workouts': [],
                'count': 0,
                'total_duration': 0,
                'total_calories': 0
            }

        type_stats[workout_type]['workouts'].append(workout)
        type_stats[workout_type]['count'] += 1
        type_stats[workout_type]['total_duration'] += workout['duration']
        type_stats[workout_type]['total_calories'] += workout['calories']

    total_workouts = len(workouts)

    print("\n" + "=" * 50)
    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    print("=" * 50)

    for workout_type, stats in type_stats.items():
        count = stats['count']
        percentage = (count / total_workouts) * 100
        avg_duration = stats['total_duration'] / count
        avg_calories = stats['total_calories'] / count

        print(f"{workout_type.capitalize()}: {count} тренировок ({percentage:.1f}%)")
        print(f"   Средняя длительность: {avg_duration:.0f} мин")
        print(f"   Средние калории: {avg_calories:.0f} ккал")

    return type_stats


def find_user_workouts(users, user_name, workouts):
    for user in users:
        if user['name'] == user_name:
            return [w for w in workouts if w['user_id'] == user['user_id']]
    return []


def analyze_user(user, workouts):
    user_workouts = []
    for workout in workouts:
        if workout['user_id'] == user['user_id']:
            user_workouts.append(workout)

    if not user_workouts:
        print(f"Пользователь {user['name']} не имеет тренировок")
        return

    total_workouts = len(user_workouts)
    total_calories = 0
    total_duration = 0
    total_distance = 0.0

    type_counts = {}

    for workout in user_workouts:
        total_calories += workout['calories']
        total_duration += workout['duration']
        total_distance += workout['distance']

        workout_type = workout['type']
        if workout_type not in type_counts:
            type_counts[workout_type] = 0
        type_counts[workout_type] += 1

    favorite_type = None
    max_count = 0
    for workout_type, count in type_counts.items():
        if count > max_count:
            max_count = count
            favorite_type = workout_type

    avg_calories = total_calories / total_workouts
    total_time = total_duration / 60

    print("\n" + "=" * 50)
    print(f"ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user['name']}")
    print("=" * 50)
    print(f"Возраст: {user['age']} лет, Вес: {user['weight']} кг")
    print(f"Уровень: {user['fitness_level']}")
    print(f"Тренировок: {total_workouts}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")
    print(f"Средние калории за тренировку: {avg_calories:.0f}")
    print(f"Любимый тип тренировки: {favorite_type}")

def visualize_workout_types_pie(workouts):

    type_counts = {}
    for workout in workouts:
        workout_type = workout['type']
        if workout_type not in type_counts:
            type_counts[workout_type] = 0
        type_counts[workout_type] += 1

    types = list(type_counts.keys())
    counts = list(type_counts.values())

    plt.figure(figsize=(10, 7))

    colors = plt.cm.Set3(range(len(types)))

    plt.pie(counts, labels=types, autopct='%1.1f%%', startangle=90,
            colors=colors, shadow=True, explode=[0.05] * len(types))

    plt.title('Распределение типов тренировок', fontsize=16, fontweight='bold')
    plt.axis('equal')  # Круглая форма
    plt.tight_layout()
    plt.show()


def visualize_user_activity_bar(user_stats):

    names = list(user_stats.keys())
    workout_counts = [stats['total_workouts'] for stats in user_stats.values()]

    plt.figure(figsize=(12, 6))

    bars = plt.bar(names, workout_counts, color='skyblue', edgecolor='black')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
                 f'{int(height)}', ha='center', va='bottom')

    plt.title('Активность пользователей (количество тренировок)',
              fontsize=16, fontweight='bold')
    plt.xlabel('Пользователи', fontsize=12)
    plt.ylabel('Количество тренировок', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


def visualize_workout_efficiency_bar(workouts):

    efficiency_data = {}

    for workout in workouts:
        workout_type = workout['type']
        efficiency = workout['calories'] / workout['duration']  # калорий/минуту

        if workout_type not in efficiency_data:
            efficiency_data[workout_type] = {'total': 0, 'count': 0}

        efficiency_data[workout_type]['total'] += efficiency
        efficiency_data[workout_type]['count'] += 1

    types = []
    avg_efficiencies = []
    for workout_type, data in efficiency_data.items():
        types.append(workout_type)
        avg_efficiencies.append(data['total'] / data['count'])

    plt.figure(figsize=(10, 6))

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']

    bars = plt.bar(types, avg_efficiencies, color=colors[:len(types)],
                   edgecolor='black')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height + 0.01,
                 f'{height:.2f}', ha='center', va='bottom', fontweight='bold')

    plt.title('Эффективность тренировок (калорий в минуту)',
              fontsize=16, fontweight='bold')
    plt.xlabel('Тип тренировки', fontsize=12)
    plt.ylabel('Калорий в минуту', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


def visualize_users_comparison_bar(user_stats):

    names = []
    calories = []
    colors = []

    color_map = {
        'продвинутый': 'red',
        'средний': 'orange',
        'начальный': 'green'
    }

    for name, stats in user_stats.items():
        names.append(name)
        calories.append(stats['total_calories'])
        colors.append(color_map.get(stats['fitness_level'], 'blue'))

    plt.figure(figsize=(12, 6))

    bars = plt.bar(names, calories, color=colors, edgecolor='black')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height + 10,
                 f'{int(height)}', ha='center', va='bottom', fontweight='bold')

    plt.title('Сравнение пользователей по общим затраченным калориям',
              fontsize=16, fontweight='bold')
    plt.xlabel('Пользователи', fontsize=12)
    plt.ylabel('Затраченные калории', fontsize=12)
    plt.xticks(rotation=45, ha='right')

    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='red', label='Продвинутый', edgecolor='black'),
        Patch(facecolor='orange', label='Средний', edgecolor='black'),
        Patch(facecolor='green', label='Начальный', edgecolor='black')
    ]
    plt.legend(handles=legend_elements, title='Уровень подготовки')

    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()

users = load_users_data()
workouts = load_workouts_data()

if not users or not workouts:
    print("Ошибка загрузки данных. Проверьте наличие файлов users.xml и workouts.xml")
    exit(0)

print("=" * 50)
print("ЛАБОРАТОРНАЯ РАБОТА 6: ОБРАБОТКА И АНАЛИЗ ДАННЫХ")
print("=" * 50)

stats = get_stats(users, workouts)

user_stats, top_users = analyze_user_activity(users, workouts)
type_stats = analyze_workout_types(workouts)

if users:
    analyze_user(users[0], workouts)


print("\n" + "=" * 50)
print("ВИЗУАЛИЗАЦИЯ ДАННЫХ С ИСПОЛЬЗОВАНИЕМ MATPLOTLIB")
print("=" * 50)


print("\n1. Круговая диаграмма типов тренировок...")
visualize_workout_types_pie(workouts)

print("\n2. Столбчатая диаграмма активности пользователей...")
visualize_user_activity_bar(user_stats)

print("\n3. Столбчатая диаграмма эффективности тренировок...")
visualize_workout_efficiency_bar(workouts)

print("\n4. Сравнительная диаграмма пользователей...")
visualize_users_comparison_bar(user_stats)

print("\n" + "=" * 50)
print("ВЫПОЛНЕНИЕ ЗАДАНИЯ ЗАВЕРШЕНО")
print("=" * 50)