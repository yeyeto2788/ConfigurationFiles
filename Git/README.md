# Configuration for git hooks

## Install dependencies:

```console
pip install pre-commit
```

## Use one of the configuration files depending on how you want to 
proceed

* Copy the `.pre-commit-config.yaml` file into the project.

## Start up the library to create the hook

```console
pre-commit install
```

## Done

Once all steps are done, doing a `git commit` it will automatically run 
this pre-commit hook.
