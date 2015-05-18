import os
import textwrap
import re

from subprocess import Popen

ENV = {
    "PATH": os.pathsep.join([
        "./dbin",
        os.environ['PATH']
    ])
}

DEFAULT_SLEDGE = textwrap.dedent("""
    $bsp_exe -game $gamedir $path\$file
    $vis_exe -game $gamedir $path\$file
    $light_exe -game $gamedir $path\$file
    cp $path\$file.bsp $bspdir\$file.bsp
    $game_exe -dev -console -allowdebug -game $gamedir +map $file
""")

# Varaibles from TeamFortress2
# --file="example"
# --ext="vmf"
# --path="c:\"
# --exedir=-"C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2"
# --bspdir="C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf\maps"
# --gamedir="C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf"
# --bsp_exe="C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\bin\vbsp.exe"
# --vis_exe="C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\bin\vvis.exe"
# --light_exe="C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\bin\vrad.exe"
# --game_exe="C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\hl2.exe"

DEFAULT_VARS = {
    # Game properties
    'exedir':   '.../Team Fortress 2',
    'gamedir':  '.../Team Fortress 2/tf',
    'bspdir':   '.../Team Fortress 2/tf/masps',

    # Binaries
    'bsp_exe':   '.../bin/bsp',
    'vis_exe':   '.../bin/vis',
    'light_exe': '.../bin/light',
    'game_exe':  '.../Team Fortress 2/hl2.exe',
    'game_exe':  '{exedir}/hl2.exe',

    # File properties
    'file': 'example_map',
    'ext':  'vmf',
    'path': '~/Desktop',
}

DOLLAR_WORDS = re.compile('\$(\w+)')

# # VBSP
#
"C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\bin\vvis.exe" -game "C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf\" -v >> C:\Users\sir\Desktop\vvis.txt



def varaibles(config_str=None, varaibles=None):
    """
        Cleverly place dollar sign words insize curly brace and use
        string format with a dict of varaibles/values

        Args:
            config_str str: Sledge script.
            varaibles dict: Variables to substitute.

        Returns:
            posix-compliant shell script
    """
    if not config_str:
        config_str = DEFAULT_SLEDGE

    if varaibles is None:
        varaibles = DEFAULT_VARS

    output = DOLLAR_WORDS.sub(r'{\1}', config_str).format( **varaibles )
    return output


# Popen(['light'], env=ENV)
print(varaibles())
