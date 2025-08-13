from pathlib import Path


def total_salary(path):
    try:
        pairs = []
        with open(path, 'r') as fh:
            for line in fh:
                try:
                    name, salary = line.strip().split(",")
                    pairs.append((name, int(salary)))
                except ValueError:
                    print(f"⚠️ Пропущено рядок через неправильний формат: {line.strip()}")

        total_sum = sum(salary for _, salary in pairs)
        average_salary = total_sum / len(pairs)
        return total_sum, average_salary

    except FileNotFoundError:
        print(f"❌ Файл {path} не знайдено.")
    except Exception as e:
        print(f"❌ Помилка при обробці файлу: {e}")


if __name__ == "__main__":
    path = Path(r"D:\GoIt\Repositories\fourth_repo\goit-algo-hw-04\First_task\salary.txt")

    total, average = total_salary(path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:.2f}")