#!/usr/bin/env python
import os
import sys
from lib.get_access_token import Get_Access_Token
from lib.create_menu import createMenu
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jiekou.settings")

    # print('5555')
    #exa = Get_Access_Token()
    #access_token = exa.get_access_token()
    #createMenu(access_token)
    print('has create menu')
    execute_from_command_line(sys.argv)
