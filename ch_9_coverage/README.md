### <span style="color: #46ab64;"> Chapter 9. Coverage.
___
AUT: [Cards (To-Do List)](https://pypi.org/project/cards/)


#### <span style="color: #46ab64;"> 1. `pytest-cov`

Installation: `pip install pytest-cov`

Coverage command: `pytest --cov=cards --cov-report=term-missing <test_path>`
`--cov={path to the code or the installed package you're testing}`


#### <span style="color: #46ab64;"> 2. `coverage`

Installation: `pip install coverage`

Coverage command: `coverage run --source=cards -m pytest <test_path>`

Report: `coverage report --show-missing`

Coverage spec file:

```text
[paths]
source = 
    path_1
    path_2
```

#### <span style="color: #46ab64;"> 3. HTML Reports

`pytest --cov=cards --cov-report=html <test_path>`

or:

`pytest --cov=cards <test_path>`

`coverage html`

#### <span style="color: #46ab64;"> 4. Excluding Code from Coverage

Code blocks can be excluded from testing with `pragma` statement.

```python
def main():
    ...


if __name__ == "__main__":  # pragma: no cover
    main()
```