import os
from typing import Union, Optional, Any
from pathlib import Path
from easydict import EasyDict as edict
from ruamel.yaml import YAML, yaml_object
from dlp import PROJ_DIR


__all__ = [
    # YAML
    'load_yaml',

    # JSON
    'load_json', 'save_json',
]


# ----------------------------------------> YAML :
# * When using the decorator, which takes the YAML() instance as a parameter,
# * the yaml = YAML() line needs to be moved up in the file -- *yaml docs*
yaml = YAML(typ='safe', pure=True)
yaml.default_flow_style = False
yaml.indent(mapping=2, sequence=4, offset=2)


@yaml_object(yaml)
class JoinPath:
    """Custom tag `!join` loader class to join strings for yaml file."""

    yaml_tag = u'!joinpath'

    def __init__(self, joined_string):
        self.joined_string = joined_string

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar(cls.yaml_tag,
                                            u'{.joined_string}'.format(node))

    @classmethod
    def from_yaml(cls, constructor, node):
        seq = constructor.construct_sequence(node)
        fullpath = Path(os.path.join(*[str(i) for i in seq])).resolve()
        return str(fullpath)


@yaml_object(yaml)
class ProjDirSetter:
    """Custom tag `!projdir` loader class for yaml file."""

    yaml_tag = u'!projdir'

    def __init__(self, path):
        self.path = path

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar(cls.yaml_tag,
                                            u'{.path}'.format(node))

    @classmethod
    def from_yaml(cls, constructor, node):
        return str(PROJ_DIR)


def load_yaml(path: Union[str, Path], pure: bool = False) -> dict:
    """config.yaml file loader.
    This function converts the config.yaml file to `dict` object.
    Args:
        path: .yaml configuration filepath
        pure: If True, just load the .yaml without converting to EasyDict
            and exclude extra info.
    Returns:
        `dict` object containing configuration parameters.
    Example:
        .. code-block:: python
            config = load_yaml("../config.yaml")
            print(config["project_name"])
    """

    path = str(Path(path).absolute().resolve())
    # * Load config file
    with open(path) as file:
        config = yaml.load(file)

    if pure == False:  # Add extra features
        # Convert dict to easydict
        config = edict(config)
    return config

# ----------------------------------------> JSON :
def load_json(path: Union[str, Path], pure: bool = False) -> edict:
    """Load .json file from given path

    Args:
        path: Path/to/the/file.json
        pure: If True, return the loaded .json content as it is.
            If False, convert it to EasyDict format
    """
    import json
    with open(path) as f:
        _data = json.load(f)
        if pure:
            return _data
        return edict(_data)


def save_json(object: Any, path: Union[str, Path]) -> None:
    """Save .json file to given path"""
    import json
    path = Path(path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(path), 'w') as f:
        json.dump(object, f)
