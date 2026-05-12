# Practice 8 — Week 8: Modules, Packages, and Unit Tests (Variant A)
# main.py contains no class definitions — it only imports from the analytics
# package and runs the program.

from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser, CountryAnalyser


if __name__ == "__main__":
    fm = FileManager("students.csv")

    if fm.check_file():
        fm.create_output_folder()

        dl = DataLoader("students.csv")
        dl.load()
        dl.preview()

        # Task 5 — polymorphism: one loop, different behaviour per class
        analysers = [GpaAnalyser(dl.students), CountryAnalyser(dl.students)]
        print("-" * 30)
        print("Running all analysers:")
        print("-" * 30)
        for analyser in analysers:
            print(analyser)              # __str__ — different per class
            analyser.analyse()           # overridden — different per class
            analyser.print_results()     # overridden — different per class
        print("-" * 30)

        # Task 4 — association: Report USES-A DataAnalyser and a ResultSaver
        saver = ResultSaver(analysers[0].result, "output/result.json")
        report = Report(analysers[0], saver)
        report.generate()
    else:
        print("Stopping program.")
