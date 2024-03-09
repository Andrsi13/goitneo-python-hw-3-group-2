from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):

    d = defaultdict(list)
    d = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }
    keys = list(d.keys())
    # today = datetime(2024, 2, 29).date()
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date*
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            next_year_bd = birthday_this_year.replace(year=today.year + 1)
        else:
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                weekday = birthday_this_year.weekday()  # день тижня на який припадє дн

                if (
                    today.weekday() == 0 and weekday > 4
                ):  # перевірка: якщо сьогодні пн і дн припадає на вихідні то його не додає в список привітань (дн повинно падати на наступний тиждень)
                    continue
                elif (
                    today.weekday() == 6 and weekday > 4
                ):  # перевірка: якщо сьогодні нд і дн припадає на вихідні то його не додає в список привітань (дн повинно падати на наступний тиждень)
                    continue
                elif (
                    weekday > 4
                ):  # перевірка: якщо дн припадає на вихідні то його додає на понеділок
                    d[keys[0]].append(name)
                else:  # решта реззульатів додаються у відповідні дні
                    d[keys[weekday]].append(name)

        result = []

        for key_day, value_name in d.items():
            if value_name:
                result.append(f"{key_day}: {", ".join(value_name)}")

    return "\n".join(result)  # список користувачів у кого дн на цьому тижні
