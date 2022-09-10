"""
Utils module.
Contains the definitions of utility functions of the program.
"""

import os


class UtilsFunc:
    """
    UtilsFunc class
    Builds an object UtilsFunc
    """

    @staticmethod
    def root_path_detector() -> str:
        """
        root_path_detector detects the root path of the program

        :return: root path of the program
        :rtype: str
        """        
        root_path = __file__.split('/')
        root_path = '/'.join(root_path[0:root_path.index('money_management')+1])
        return root_path

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
        pass
