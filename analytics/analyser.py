# Practice 7 — Advanced OOP. DataAnalyser is the base class; GpaAnalyser is the
# Variant A child that overrides analyse() and print_results(). CountryAnalyser
# is a second child of a different variant, used only so the polymorphism loop
# in main.py has more than one analyser type. (Practice 8 puts these in a module.)


# Task 1 — base class
class DataAnalyser:
    """Base class — defines the shared structure every analyser variant inherits."""

    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        # Overridden in every child class.
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


# Task 2 — child class for Variant A
class GpaAnalyser(DataAnalyser):
    """Variant A — GPA statistics: average, max, min, count of high performers."""

    def __init__(self, students):
        super().__init__(students)

    # Overrides DataAnalyser.analyse() — computes the result, stays silent.
    def analyse(self):
        gpas = []
        high_performers = 0

        for student in self.students:
            try:
                gpa = float(student["GPA"])
            except (TypeError, ValueError):
                student_id = student.get("student_id", "Unknown")
                print(f"Warning: could not convert GPA for student {student_id} — skipping row.")
                continue

            gpas.append(gpa)
            if gpa > 3.5:
                high_performers += 1

        self.result.clear()
        self.result.update({
            "total_students": len(self.students),
            "average_gpa": round(sum(gpas) / len(gpas), 2) if gpas else 0,
            "max_gpa": max(gpas) if gpas else 0,
            "min_gpa": min(gpas) if gpas else 0,
            "high_performers": high_performers,
        })

    # Task 3 — override print_results(): formatted header/footer around the
    # base-class output produced by super().print_results().
    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"


class CountryAnalyser(DataAnalyser):
    """Variant B — country analysis (used here as the second analyser type for
    the polymorphism task in Practice 7)."""

    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        country_counts = {}

        for student in self.students:
            country = student.get("country", "Unknown")
            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1

        top_3 = sorted(country_counts.items(), key=lambda kv: kv[1], reverse=True)[:3]

        self.result.clear()
        self.result.update({
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3": top_3,
        })

    def print_results(self):
        print("=" * 30)
        print("COUNTRY ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"
