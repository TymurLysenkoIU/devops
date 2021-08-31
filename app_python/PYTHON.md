# Python

## Good practices

### 1. Use `requirements.txt` to manage python dependencies

Applications need dependencies to be present before running. The easiest way to get the dependencies is to use language's corresponding package manager and keep all the dependencies in a special file that is used by package manager to install dependencies.

### 2. Specify versions of the packages explicitly

When a new version is issued and its version is not specified explicitly it is not possible to get reproducible build anymore, because the new version might be incompatible in some way with the actual version of the package used to write the application.

### (Bonus) Use strongly typed languages for real applications (i.e., preferably not python) :)

## Testing

All tests are located in the `tests` python package. The dependencies initialization is located in `conftest.py`, i.e. the flask application test client is being created there and used by other tests. All files containing tests start with `test_*`, so that `pytest` can find them.

### Good practices

#### 1. Write testable code

Not all code written is easy to test. One needs to separate business logic from the implementation, and specify dependencies for business logic explicitly, so that each part of the business logic can be tested independently. Thus, it makes sense to create separate services (e.g. classes) and pass them as dependencies to other services (e.g. in constructors).

#### 2. Don't deploy tests to the resulting build

Tests only sense during the development process. Once the development of a feature is finished and all tests are passed the tests are no longer needed in the resulting application build, thus to not include extraneous dependencies that won't be needed they should not be included in the final build.

#### 3. Run all tests after making changes to the code

This is what tests are meant to be written for. In order to be sure that one did not change the existing behaviour of the application after making changes the tests need to be run, because they specify the desired behaviour.

#### 4. Regression testing

If there was a bug in the code in the past, add the corresponding test to the test suit, so that in the future we are sure that the case was fixed and works.
