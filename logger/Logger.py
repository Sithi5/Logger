from enum import IntEnum, auto, Enum
from typing import Literal


class Colors(Enum):
    """Enumerate Logger Level. Ordered from the most critical to the least"""

    RED = "\033[91m"
    PURPLE = "\033[95m"
    YELLOW = "\033[93m"
    END = "\033[0m"


class LoggerLevelEnum(IntEnum):
    """Enumerate Logger Level. Ordered from the most critical to the least"""

    ERROR = auto()
    CRITICAL = auto()
    WARNING = auto()
    DEBUG = auto()
    INFO = auto()


LevelType = Literal["INFO", "DEBUG", "WARNING", "CRITICAL", "ERROR"]
DefaultType = "INFO"


class Logger:
    """
    Simple Logger class inspired by the Logger base module of python.

    Methods
    -------
    __init__(level: LevelType = DefaultType):
        Constructs all the necessary attributes for the Logger object.

    info(*args)

    debug(*args)

    warning(*args)

    critical(*args)

    error(*args)
    """

    _string_level_to_print: str = ""

    def __init__(
        self,
        level: LevelType = DefaultType,
        colors: bool = True,
        display_levels: bool = True,
    ):
        """
        Constructs all the necessary attributes for the Logger object.

        Parameters
        ----------
            level : The level of severity you want to display:
                "INFO" (default)
                "DEBUG"
                "WARNING"
                "CRITICAL"
                "ERROR",
            colors : Set to false if you want to disable the color of prints.
            display_levels : Set to false if you want to disable the display of level severity.
        """

        self.level = level
        self._colors = colors
        self._display_levels = display_levels

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value: LevelType = DefaultType):
        self._level = LoggerLevelEnum[value.upper()]

    def _addColorToPrint(self, buff: str):
        """
        Add color to the output string.
        This method should be called in last.
        """
        return self._color_ANSI_escape_code + buff + Colors.END.value

    def _addLevelToPrint(self, buff: str):
        return self._string_level_to_print + buff

    def _rootLogger(
        self,
        *args,
        level: LevelType,
    ):
        buff = ""
        if self._level >= level:
            for arg in args:
                if len(buff) != 0:
                    buff += " " + str(arg)
                else:
                    buff += str(arg)
            if self._display_levels is True:
                buff = self._addLevelToPrint(buff=buff)
            if self._colors is True:
                buff = self._addColorToPrint(
                    buff=buff,
                )
            print(buff)

    def info(self, *args):
        """
        Log a message with severity 'INFO' on the root logger.
        """
        self._string_level_to_print = "INFO: "
        self._color_ANSI_escape_code = ""
        self._rootLogger(
            *args,
            level=LoggerLevelEnum.INFO.value,
        )

    def debug(self, *args):
        """
        Log a message with severity 'DEBUG' on the root logger.
        """
        self._string_level_to_print = "DEBUG: "
        self._color_ANSI_escape_code = Colors.PURPLE.value
        self._rootLogger(
            *args,
            level=LoggerLevelEnum.DEBUG.value,
        )

    def warning(self, *args):
        """
        Log a message with severity 'WARNING' on the root logger.
        """
        self._string_level_to_print = "WARNING: "
        self._color_ANSI_escape_code = Colors.YELLOW.value
        self._rootLogger(
            *args,
            level=LoggerLevelEnum.WARNING.value,
        )

    def critical(self, *args):
        """
        Log a message with severity 'CRITICAL' on the root logger.
        """
        self._string_level_to_print = "CRITICAL: "
        self._color_ANSI_escape_code = Colors.RED.value
        self._rootLogger(
            *args,
            level=LoggerLevelEnum.CRITICAL.value,
        )

    def error(self, *args):
        """
        Log a message with severity 'ERROR' on the root logger.
        """
        self._string_level_to_print = "ERROR: "
        self._color_ANSI_escape_code = Colors.RED.value
        self._rootLogger(
            *args,
            level=LoggerLevelEnum.ERROR.value,
        )
