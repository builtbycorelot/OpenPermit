# Contributing to OpenPermit

We love your input! We want to make contributing to OpenPermit as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## We Develop with Github
We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Setting up for Testing


Install development dependencies for both Node and Python tooling:

```bash
npm install                 # install Node packages
pip install -r requirements-dev.txt  # Python test utilities
```

### Running the Node tests

Execute the bundled unit tests with:

```bash
npm test
```

### Running Playwright

Browser checks use [Playwright](https://playwright.dev). Install its runtime and run the tests:

```bash
npx playwright install
npx playwright test
```

### Python schema validation

The `open-data-layer` folder includes a validator script. Run it or the `pytest` suite to confirm schema compliance:

```bash
pytest                     # run all Python unit tests
python open-data-layer/schema/validate_schema.py
```
## Pull Request Process
1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Update the documentation
4. Ensure any install or build dependencies are removed
5. Issue that pull request!

## Any contributions you make will be under the Software License
In short, when you submit code changes, your submissions are understood to be under the same license that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using Github's [issue tracker]
We use GitHub issues to track public bugs. Report a bug by opening a new issue!

## License
By contributing, you agree that your contributions will be licensed under its MIT License.

## References
This document was adapted from the open-source contribution guidelines for [Facebook's Draft](https://github.com/facebook/draft-js/blob/master/CONTRIBUTING.md).
