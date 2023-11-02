"""
Utils module.
Contains the definitions of utility functions of the program.
"""

# pylint: disable=invalid-name

import os

from bam.pymodules.bam_enumerators import (ColorMenuBgEnum, ColorMenuFgEnum,
                                           LanguageEnum)


class Utils:
    """Utils class containing general purpose static methods of the program

    Returns:
        Utils: instance of Utils class
    """

    @staticmethod
    def root_path_detector() -> str:
        """Detects the rooth path directory of the program

        Returns:
            str: root_path_detector detects the root path of the program

        """

        return os.getcwd()

    @staticmethod
    def string_to_language_enum(lang: str) -> LanguageEnum:
        """Map the input string to the Enum with equal value

        Args:
            lang (str): input string

        Returns:
            LanguageEnum: output enum
        """
        for x in LanguageEnum:
            if lang == x.value:
                return x

        return LanguageEnum.ENGLISH

    @staticmethod
    def string_to_color_menu_bg_enum(color: str) -> ColorMenuBgEnum:
        """Map the input string to the Enum with equal value

        Args:
            color (str): input string

        Returns:
            ColorMenuBgEnum: output enum
        """
        for x in ColorMenuBgEnum:
            if color == x.value:
                return x

        return ColorMenuBgEnum.GREEN

    @staticmethod
    def string_to_color_menu_fg_enum(color: str) -> ColorMenuFgEnum:
        """Map the input string to the Enum with equal value

        Args:
            color (str): input string

        Returns:
            ColorMenuFgEnum: output enum
        """
        for x in ColorMenuFgEnum:
            if color == x.value:
                return x

        return ColorMenuFgEnum.GRAY

    @staticmethod
    def print_title(value: str) -> None:
        """
        print_title Fancy print of a title
        """
        os.system("clear")
        header_line = "="*40
        print(header_line, flush=True)
        print(f"  {value}", flush=True)
        print(header_line, flush=True)

    # TODO: implement data backup function
    @staticmethod
    def data_backup() -> None:
        """
        data_backup method to create a data backup
        """
