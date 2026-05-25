
from geometry3 import (
    Triangle, Rectangle, Trapeze, Parallelogram, Circle,
    Ball, TriangularPyramid, QuadrangularPyramid,
    RectangularParallelepiped, Cone, TriangularPrism
)


def find_largest_figure(filename):
    mapping = {
        "Triangle": Triangle,
        "Rectangle": Rectangle,
        "Trapeze": Trapeze,
        "Parallelogram": Parallelogram,
        "Circle": Circle,
        "Ball": Ball,
        "TriangularPyramid": TriangularPyramid,
        "QuadrangularPyramid": QuadrangularPyramid,
        "RectangularParallelepiped": RectangularParallelepiped,
        "Cone": Cone,
        "TriangularPrism": TriangularPrism
    }

    max_figure_name = None
    max_volume = -1.0
    best_raw_line = ""

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line_cleaned = line.strip()
                if not line_cleaned:
                    continue

                parts = line_cleaned.split()
                fig_name = parts[0]

                if fig_name not in mapping:
                    continue

                try:
                    args = [float(x) for x in parts[1:]]
                    fig_object = mapping[fig_name](*args)
                    current_volume = fig_object.volume()

                    if current_volume > max_volume:
                        max_volume = current_volume
                        max_figure_name = fig_name
                        best_raw_line = line_cleaned
                except Exception:
                    continue

    except FileNotFoundError:
        print("Помилка")
        return None

    return max_figure_name, max_volume, best_raw_line


if __name__ == "__main__":
    files_to_process = ["input01.txt", "input02.txt", "input03.txt"]

    print("РЕЗУЛЬТАТИ АНАЛІЗУ")

    for current_file in files_to_process:
        analysis_result = find_largest_figure(current_file)
        if analysis_result:
            name, vol, raw_data = analysis_result
            print(f"Файл: {current_file}")
            print(f" Найбільша фігура за мірою : {name}")
            print(f" Значення міри (об'єм/площа): {vol:.4f}")
            print(f" Рядок у файлі: '{raw_data}'")
