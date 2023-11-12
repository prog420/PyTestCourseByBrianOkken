### <span style="color: #46ab64;"> Chapter 10. Mocks.
___
AUT: [Cards (To-Do List)](https://pypi.org/project/cards/)


#### <span style="color: #46ab64;"> 1. `unittest.mock`

```python
import cards
from unittest import mock


def test_mock_path():
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        MockCardsDB.return_value.path.return_value = "/mock_path"
        with cards.cli.cards_db() as db:
            print(f"db.path() = {db.path()}")
```


#### <span style="color: #46ab64;"> 2. Syncing Mock and Implementation with Autospec


**Issue:** Mock objects are too flexible by default.
They can accept misspelled methods, additional parameters, etc.
It can cause _mock drift_. Mock drift occurs when the mocked interface changes and your mock does not.

**Solution:** use `mock.patch.object(..., autospec=True)`

#### <span style="color: #46ab64;"> 3. Side Effects

`mock_object.side_effect = Exception`


#### <span style="color: #46ab64;"> 4. Patch and where to Patch

1. Mocking function (`isleap()`) in `calendar` using `patch()`:
```python
import calendar
from unittest.mock import patch

with patch('calendar.isleap'):
    print(calendar.isleap(1995))

...
# <MagicMock name='isleap()' id='2641389555088'>
```

2. Mocking directly imported function:

```python
from calendar import isleap
from unittest.mock import patch

with patch('calendar.is_weekday'):
    print(isleap(1995))

...
# False
```

Function won't be mocked because `from calendar import is_weekday`
binds the real function to the local scope.
So,even though you `patch` the function later, your mock will be ignored
because you already have a local reference to the un-mocked function.

A good rule of thumb is to patch the object where it is looked up.

**Working example of mocking directly imported function:**

```python
from calendar import isleap
from unittest.mock import patch

with patch('__main__.is_weekday'):
    print(isleap(1995))

...
# <MagicMock name='isleap()' id='2641389555088'>
```