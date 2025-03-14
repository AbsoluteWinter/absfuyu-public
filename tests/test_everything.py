"""
Test: Everything

Version: 5.2.0
Date updated: 16/03/2025 (dd/mm/yyyy)
"""

# Library
# ---------------------------------------------------------------------------
import pytest

try:  # [beautiful] feature
    import rich  # type: ignore
except ImportError:
    rich = pytest.importorskip("rich")


# --- Loading test --------------------------------------------------------
from absfuyu import __author__, __license__, __title__, __version__
from absfuyu.config import (
    _SPACE_REPLACE,
    ABSFUYU_CONFIG,
    Config,
    ConfigFormat,
    Setting,
    SettingDictFormat,
)
from absfuyu.core import (
    BaseClass,
    CLITextColor,
    ShowAllMethodsMixin,
    __package_feature__,
    deprecated,
    tqdm,
    unidecode,
    versionadded,
    versionchanged,
)
from absfuyu.core.baseclass import (
    AutoREPRMixin,
    MethodNPropertyList,
    MethodNPropertyResult,
    PositiveInitArgsMeta,
)
from absfuyu.core.baseclass2 import (
    PerformanceTrackingMeta,
    ShowAllMethodsMixinInspectVer,
    positive_class_init_args,
)
from absfuyu.core.decorator import (
    add_subclass_methods_decorator,
    dummy_decorator,
    dummy_decorator_with_args,
)
from absfuyu.core.docstring import (
    _SPHINX_DOCS_TEMPLATE,
    SphinxDocstring,
    SphinxDocstringMode,
)
from absfuyu.core.dummy_func import dummy_function
from absfuyu.dxt import (
    DictAnalyzeResult,
    DictBoolFalse,
    DictBoolTrue,
    DictExt,
    IntExt,
    ListExt,
    ListNoDunder,
    ListREPR,
    Text,
    TextAnalyzeDictFormat,
)
from absfuyu.extra import is_loaded
from absfuyu.extra.beautiful import BeautifulOutput  # Has rich
from absfuyu.extra.da.dadf import (  # Has pandas, numpy
    DADF,
    DataAnalystDataFrameCityMixin,
    DataAnalystDataFrameColumnMethodMixin,
    DataAnalystDataFrameDateMixin,
    DataAnalystDataFrameInfoMixin,
    DataAnalystDataFrameNAMixin,
    DataAnalystDataFrameOtherMixin,
    DataAnalystDataFrameRowMethodMixin,
)
from absfuyu.extra.da.dadf_base import (  # Has pandas, numpy
    CityData,
    DataAnalystDataFrameBase,
    SplittedDF,
)
from absfuyu.extra.da.mplt import MatplotlibFormatString, _PLTFormatString
from absfuyu.extra.data_analysis import (  # Has pandas, numpy
    compare_2_list,
    equalize_df,
    rename_with_dict,
)
from absfuyu.fun import happy_new_year, human_year_to_dog_year, zodiac_sign
from absfuyu.fun.tarot import Tarot, TarotCard
from absfuyu.game import GameStats, game_escapeLoop, game_RockPaperScissors
from absfuyu.game.sudoku import Sudoku
from absfuyu.game.tictactoe import GameMode, TicTacToe
from absfuyu.game.wordle import Wordle  # Has requests

# --- Sub-package ---
from absfuyu.general.content import (  # Has unidecode
    Content,
    ContentLoader,
    LoadedContent,
)
from absfuyu.general.human import BloodType, Human, Person
from absfuyu.general.shape import (
    Circle,
    Cube,
    Cuboid,
    Cylinder,
    EqualSidesPolygon,
    HemiSphere,
    Hexagon,
    Parallelogram,
    Pentagon,
    Polygon,
    Rectangle,
    Rhombus,
    Shape,
    Sphere,
    Square,
    ThreeDimensionShape,
    Trapezoid,
    Triangle,
)

# from absfuyu.logger import *
from absfuyu.logger import LogLevel, compress_for_log, logger
from absfuyu.pkg_data import BasicLZMAOperation, DataList, DataLoader, Pickler
from absfuyu.sort import binary_search, insertion_sort, linear_search, selection_sort

# from absfuyu.tools import *
from absfuyu.tools.checksum import Checksum, ChecksumMode
from absfuyu.tools.converter import (
    Base64EncodeDecode,
    ChemistryElement,
    Str2Pixel,
    Text2Chemistry,
)
from absfuyu.tools.generator import Charset, Generator
from absfuyu.tools.inspector import Inspector, inspect_all
from absfuyu.tools.keygen import Keygen
from absfuyu.tools.obfuscator import Obfuscator, StrShifter
from absfuyu.tools.passwordlib import TOTP, PasswordGenerator, PasswordHash
from absfuyu.tools.shutdownizer import (
    ShutdownEngine,
    ShutdownEngineLinux,
    ShutdownEngineMac,
    ShutdownEngineWin,
    ShutDownizer,
)
from absfuyu.tools.web import gen_random_commit_msg, soup_link  # Has bs4, requests
from absfuyu.typings import _CALLABLE, CT, N, P, R, SupportsShowMethods, T, _Number
from absfuyu.util import (
    get_installed_package,
    set_max,
    set_min,
    set_min_max,
    stop_after_day,
)
from absfuyu.util.api import APIRequest, ping_windows  # Has requests
from absfuyu.util.json_method import JsonFile
from absfuyu.util.lunar import LunarCalendar
from absfuyu.util.path import (
    Directory,
    DirectoryArchiverMixin,
    DirectoryBase,
    DirectoryBasicOperationMixin,
    DirectoryInfo,
    DirectoryInfoMixin,
    DirectoryOrganizerMixin,
    DirectoryTreeMixin,
    FileOrFolderWithModificationTime,
    SaveFileAs,
)
from absfuyu.util.performance import (
    Checker,
    function_benchmark,
    function_debug,
    measure_performance,
    retry,
)
from absfuyu.util.shorten_number import (
    CommonUnitSuffixesFactory,
    Decimal,
    UnitSuffixFactory,
    shorten_number,
)
from absfuyu.util.text_table import (
    BoxDrawingCharacter,
    BoxDrawingCharacterBold,
    BoxDrawingCharacterDashed,
    BoxDrawingCharacterDouble,
    OneColumnTableMaker,
)
from absfuyu.version import (
    Bumper,
    PkgVersion,
    ReleaseLevel,
    ReleaseOption,
    Version,
    VersionDictFormat,
)


# Test
# ---------------------------------------------------------------------------
def test_everything():
    assert True
