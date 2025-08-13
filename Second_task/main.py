from pathlib import Path


def get_cats_info(path):
    try:
        cats_list = []
        with open(path, 'r') as fh:
            for line in fh:
                cat_id, cat_name, cat_age = line.strip().split(",", 2)
                cat_info = {
                    "id": cat_id,
                    "name": cat_name,
                    "age": cat_age
                            }
                cats_list.append(cat_info)

        return cats_list

    except FileNotFoundError:
        print(f"❌ Файл {path} не знайдено.")
    except Exception as e:
        print(f"❌ Помилка при обробці файлу: {e}")



if __name__ == "__main__":
    path = Path(r"D:\GoIt\Repositories\fourth_repo\goit-algo-hw-04\Second_task\cats.txt")

    cats_info = get_cats_info(path)
    print(cats_info)