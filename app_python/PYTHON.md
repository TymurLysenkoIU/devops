# Python

## Good practices

### 1. Use `requirements.txt` to manage python dependencies

Applications need dependencies to be present before running. The easiest way to get the dependencies is to use language's corresponding package manager and keep all the dependencies in a special file that is used by package manager to install dependencies.

### 2. Specify versions of the packages explicitly

When a new version is issued and its version is not specified explicitly it is not possible to get reproducible build anymore, because the new version might be incompatible in some way with the actual version of the package used to write the application.

### (Bonus) Use strongly typed languages for real applications (i.e., preferably not python) :)

## Testing

### Good practices

- [ ] TODO: describe
