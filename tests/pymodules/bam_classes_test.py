"""Unit test module for ultil.py

Author: @aeroanselm
"""

# pylint: disable=import-error
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest

from bam.pymodules.bam_classes import ProgramSettings
from bam.pymodules.bam_enumerators import (ColorMenuBgEnum, ColorMenuFgEnum,
                                           LanguageEnum)


class ProgramSettingTest(unittest.TestCase):

    def test_get_language(self) -> None:
        program_settings = ProgramSettings()
        program_settings.set_language(language=LanguageEnum.ITALIANO)
        program_settings.set_terminal_bg_color(
            terminal_bg_color=ColorMenuBgEnum.BLACK)
        program_settings.set_terminal_fg_color(
            terminal_fg_color=ColorMenuFgEnum.BLACK)

        self.assertEqual(program_settings.get_language(),
                         LanguageEnum.ITALIANO)
        self.assertEqual(
            program_settings.get_terminal_bg_color(), ColorMenuBgEnum.BLACK)
        self.assertEqual(
            program_settings.get_terminal_fg_color(), ColorMenuFgEnum.BLACK)


if __name__ == "__main__":
    unittest.main()
