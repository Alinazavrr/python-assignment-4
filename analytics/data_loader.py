import csv


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.students = list(reader)

            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return []
        except Exception as error:
            print(f"Unexpected error while loading data: {error}")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)
        for student in self.students[:n]:
            print(
                f"{student['student_id']} | {student['age']} | {student['gender']} | "
                f"{student['country']} | GPA: {student['GPA']}"
            )
        print("-" * 30)
