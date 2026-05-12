# python-assignment-4

Astana IT University — Python Programming, Practices 7 & 8 (Variant A).

Practice 8 is Practice 7 refactored into modules and a package, so this repo is the
final state — the `analytics/` package and `main.py` contain all of the Practice 7
work (base class, child class, `print_results()` override, `Report` association,
polymorphism), plus the Practice 8 module/package split and unit tests.

## Project structure

```
python-assignment-4/
├── students.csv            University Students Performance & Study Habits dataset (10 000 rows)
├── main.py                 entry point — imports from the package and runs the program
├── analytics/              the package
│   ├── __init__.py         re-exports FileManager, DataLoader, DataAnalyser, ResultSaver, Report
│   ├── file_manager.py     FileManager — checks the CSV exists, creates output/
│   ├── data_loader.py      DataLoader  — reads the CSV with csv.DictReader, previews rows
│   ├── analyser.py         DataAnalyser (base) + GpaAnalyser (Variant A) + CountryAnalyser
│   ├── result_saver.py     ResultSaver — writes the result dict to JSON
│   └── report.py           Report — association (USES-A) of a DataAnalyser and a ResultSaver
├── tests/
│   ├── __init__.py
│   └── test_analyser.py    4 unittest tests for GpaAnalyser (the run output is pasted at the top)
├── output/result.json      written when you run main.py
└── .gitignore
```

## What it does

`main.py`:

1. `FileManager("students.csv")` — checks the file exists, creates the `output/` folder.
2. `DataLoader("students.csv")` — loads the CSV, prints the first 5 rows.
3. Builds `analysers = [GpaAnalyser(...), CountryAnalyser(...)]` and loops over them
   calling `print(analyser)`, `analyser.analyse()`, `analyser.print_results()` — the
   same three calls give different output per class (**polymorphism**).
4. `Report(analysers[0], saver).generate()` — runs the analyser, prints its results,
   and saves the result dict to `output/result.json` (**association**).

`GpaAnalyser` (Variant A) computes `total_students`, `average_gpa`, `max_gpa`,
`min_gpa`, and `high_performers` (students with GPA > 3.5) and stores them in
`self.result`. `DataAnalyser.print_results()` prints the dict as `key: value`;
`GpaAnalyser.print_results()` wraps that with a formatted header and footer.

## How to run

From the project root:

```bash
python main.py                                # run the program
python -m unittest tests/test_analyser.py -v  # run the unit tests
```

(All four tests pass — the captured output is in the comment block at the top of
`tests/test_analyser.py`.)

## Dataset

`students.csv` is the *University Students Performance & Study Habits* dataset
(10 000 rows, 27 columns: `student_id`, `age`, `gender`, `country`, `major`, `GPA`,
`study_hours_per_day`, …). It is included here so the program runs after cloning.
