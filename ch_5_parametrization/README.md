### <span style="color: #46ab64;"> Chapter 5. Parametrization
___
AUT: [Cards (To-Do List)](https://pypi.org/project/cards/)

1. Function parametrization
2. Fixture parametrization
3. Hooks (`pytest_generate_tests`)

#### <span style="color: #46ab64;"> 1.1 `pytest_generate_tests` & `Metafunc`

* We could base parametrization list on a command-line flag:

`metafunc.config.getoption("--someflag")`

* We could parametrize multiple parameters:

`metafunc.paramterize("planet, moon", [
    ('Earth', 'Moon'), 
    ('Mars', 'Deimos'),
    ('Mars', 'Phobos),
])`


#### <span style="color: #46ab64;"> 1.2 Running subset of tests

1. Parameteres can be used to gather a smaller subset of tests:

`pytest -v -k todo` 

`pytest -v -k "todo and not (done or play)"`