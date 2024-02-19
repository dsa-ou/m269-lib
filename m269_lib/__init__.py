"""This is a pedagogical algorithms and data structures library.

It currently implements the Stack and Queue abstract data types (ADTs).

To install the library in the currently active environment, enter in a terminal:
```bash
pip install m269-lib
```
To learn how to use the library, see the examples in the documentation of the classes.

The code repository is at https://github.com/dsa-ou/m269-lib.

## Licence

`m269-lib` is Copyright © 2024 by The Open University, UK.
The code is licensed under a [BSD 3-clause licence](https://github.com/dsa-ou/m269-lib/blob/main/LICENSE).
The documentation is licensed under a
[Creative Commons Attribution 4.0 International Licence](http://creativecommons.org/licenses/by/4.0).
"""

# Import all classes so that they can be directly imported from m269_lib.
# Provide short names for the recommended implementations.
from .queue import *
from .queue import LinkedListQueue as Queue
from .stack import *
from .stack import PythonListStack as Stack
