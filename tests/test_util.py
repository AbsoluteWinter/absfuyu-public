"""
Test: Util

Version: 5.2.0
Date updated: 15/03/2025 (dd/mm/yyyy)
"""

from pathlib import Path

import pytest

from absfuyu.config import CONFIG_PATH
from absfuyu.util import set_max, set_min, set_min_max
from absfuyu.util.json_method import JsonFile
from absfuyu.util.path import Directory


# MARK: util
@pytest.mark.abs_util
class TestUtil:
    """absfuyu.util"""

    @pytest.mark.skip
    @pytest.mark.parametrize(["value", "output"], [(10, 10), (-5, 0)])
    def test_set_min(self, value: int, output: int) -> None:
        assert set_min(value, min_value=0) == output

    @pytest.mark.skip
    @pytest.mark.parametrize(["value", "output"], [(200, 100), (10, 10)])
    def test_set_max(self, value: int, output: int) -> None:
        assert set_max(value, max_value=100) == output

    @pytest.mark.parametrize(["value", "output"], [(50, 50), (-10, 0), (200, 100)])
    def test_set_min_max(self, value: int, output: int) -> None:
        assert set_min_max(value, min_value=0, max_value=100) == output


# MARK: json
@pytest.mark.abs_util
class TestUtilJsonMethod:
    """absfuyu.util.json_method"""

    def test_json_load(self) -> None:
        instance = JsonFile(CONFIG_PATH)
        loaded = instance.load_json()
        assert isinstance(loaded, dict)


# MARK: path
@pytest.mark.abs_util
class TestUtilPath:
    """absfuyu.util.path"""

    @pytest.mark.skip  # This takes too long
    def test_list_structure(self) -> None:
        instance = Directory(source_path=Path.cwd())
        assert instance.list_structure_pkg()
