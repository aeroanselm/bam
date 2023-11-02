"""Unit test module for ultil.py

Author: @aeroanselm
"""

# pylint: disable=import-error
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import os
import unittest

from bam.common.utils import Utils
from bam.pymodules.bam_enumerators import (ColorMenuBgEnum, ColorMenuFgEnum,
                                           LanguageEnum)


class UtilsTest(unittest.TestCase):

    def test_root_path_detector(self) -> None:

        self.assertEqual(Utils.root_path_detector(), os.getcwd())

    def test_string_to_language_enum(self) -> None:

        self.assertEqual(LanguageEnum.ENGLISH,
                         Utils.string_to_language_enum(lang='en'))
        self.assertEqual(LanguageEnum.ITALIANO,
                         Utils.string_to_language_enum(lang='it'))

    def test_string_to_color_menu_bg_enum(self) -> None:

        self.assertEqual(ColorMenuBgEnum.BLACK,
                         Utils.string_to_color_menu_bg_enum(color='bg_black'))
        self.assertEqual(ColorMenuBgEnum.BLUE,
                         Utils.string_to_color_menu_bg_enum(color='bg_blue'))
        self.assertEqual(ColorMenuBgEnum.CYAN,
                         Utils.string_to_color_menu_bg_enum(color='bg_cyan'))
        self.assertEqual(ColorMenuBgEnum.GRAY,
                         Utils.string_to_color_menu_bg_enum(color='bg_gray'))
        self.assertEqual(ColorMenuBgEnum.GREEN,
                         Utils.string_to_color_menu_bg_enum(color='bg_green'))
        self.assertEqual(ColorMenuBgEnum.PURPLE,
                         Utils.string_to_color_menu_bg_enum(color='bg_purple'))
        self.assertEqual(ColorMenuBgEnum.RED,
                         Utils.string_to_color_menu_bg_enum(color='bg_red'))
        self.assertEqual(ColorMenuBgEnum.YELLOW,
                         Utils.string_to_color_menu_bg_enum(color='bg_yellow'))

    def test_string_to_color_menu_fg_enum(self) -> None:

        self.assertEqual(ColorMenuFgEnum.BLACK,
                         Utils.string_to_color_menu_fg_enum(color='fg_black'))
        self.assertEqual(ColorMenuFgEnum.BLUE,
                         Utils.string_to_color_menu_fg_enum(color='fg_blue'))
        self.assertEqual(ColorMenuFgEnum.CYAN,
                         Utils.string_to_color_menu_fg_enum(color='fg_cyan'))
        self.assertEqual(ColorMenuFgEnum.GRAY,
                         Utils.string_to_color_menu_fg_enum(color='fg_gray'))
        self.assertEqual(ColorMenuFgEnum.GREEN,
                         Utils.string_to_color_menu_fg_enum(color='fg_green'))
        self.assertEqual(ColorMenuFgEnum.PURPLE,
                         Utils.string_to_color_menu_fg_enum(color='fg_purple'))
        self.assertEqual(ColorMenuFgEnum.RED,
                         Utils.string_to_color_menu_fg_enum(color='fg_red'))
        self.assertEqual(ColorMenuFgEnum.YELLOW,
                         Utils.string_to_color_menu_fg_enum(color='fg_yellow'))


if __name__ == "__main__":
    unittest.main()
