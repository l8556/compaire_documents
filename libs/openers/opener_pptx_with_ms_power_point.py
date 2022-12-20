# -*- coding: utf-8 -*-
from loguru import logger
from rich import print

from configuration import version
from framework.power_point import PowerPoint


class OpenerPptx(PowerPoint):
    def run_opener(self, list_of_files):
        logger.info(f'Opener {self.doc_helper.converted_extension} with ms PP on version: {version} is running.')
        for self.doc_helper.converted_file in list_of_files:
            if not self.doc_helper.converted_file.lower().endswith(".pptx"):
                continue
            self.doc_helper.preparing_files_for_opening_test()
            print(f'[bold green]In test[/] {self.doc_helper.converted_file}')
            self.open_presentation_with_cmd(self.doc_helper.tmp_converted_file)
            self.errors_handler_when_opening()
            self.close_presentation_with_hotkey()
            self.doc_helper.tmp_cleaner()
