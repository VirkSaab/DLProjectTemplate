# DLProjectTemplate

### If Python 3.8 is not installed on your system. Replace 3.x to your desired Python 3 version. Make sure you also change the Python version in `Makefile` as well to use `make make_venv` command.
```bash
apt update
apt install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt update
apt install python3.8 python3.8-venv python3.8-dev
```
### Create a virtual environment
```bash
make make_venv
```
```bash
source venv/bin/activate
```

## Project Documentation using Sphinx:
* create docs:
    ```bash
        sphinx-quickstart docs
    ```
* say yes to this: `> Separate source and build directories (y/n) [n]: y`
* Add these to `docs/source/conf.py` for Google style documentation. See example [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
    ```python
        extensions = [
            'sphinx.ext.duration',
            'sphinx.ext.autodoc',
            'sphinx.ext.napoleon'
        ]
        # Napoleon settings
        napoleon_google_docstring = True
        napoleon_numpy_docstring = False
        napoleon_include_init_with_doc = False
        napoleon_include_private_with_doc = False
        napoleon_include_special_with_doc = True
        napoleon_use_admonition_for_examples = False
        napoleon_use_admonition_for_notes = False
        napoleon_use_admonition_for_references = False
        napoleon_use_ivar = False
        napoleon_use_param = True
        napoleon_use_rtype = True
        napoleon_preprocess_types = False
        napoleon_type_aliases = None
        napoleon_attr_annotations = True

        # Documentation theme
        html_theme = 'furo'
    ```
* Then
    ```bash
        cd docs
        sphinx-build -b html source/ build/html
        sphinx-apidoc -o source/ ../dlp --force
        make html
    ```
* Some sources for errors in sphinx - [sphinx-docs](https://www.sphinx-doc.org/en/master/tutorial/index.html), [fix 1](https://stackoverflow.com/questions/13516404/sphinx-error-unknown-directive-type-automodule-or-autoclass).