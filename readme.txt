.-..-.   .-..----.  .----. .----.  .---. 
| ||  `.'  || {}  }/  {}  \| {}  }{_   _}
| || |\ /| || .--' \      /| .-. \  | |  
`-'`-' ` --'`-'     `----' `-' `-'  `-'  
****************************************
*_____  ____   ____   ____  ____ _____ *
*| () )| ===| / () \ | _) \| ===|| () )*
*|_|\_\|____|/__/\__\|____/|____||_|\_\*
****************************************
             ...reader...

-- ABOUT --
The reader library is used for reading and viewing files.
Developed by StarShot Studios.

Reader consists of 4 modules:
| rfiles - File operations and process management
| rhtml  - Web browsing and HTML content retrieval
| raudio - Audio playback and control
| rmouse - Mouse movement and clicking

-- RFILES --
rfiles.create(filename, content)  - Create a file with content
rfiles.read(filename)             - Read file contents
rfiles.write(filename, content)   - Write to a file
rfiles.append(filename, content)  - Append to a file
rfiles.delete(filename)           - Delete a file
rfiles.exists(filename)           - Check if file exists
rfiles.run(program)               - Run a program/file
rfiles.stop(program_name)         - Stop a running program

-- RHTML --
rhtml.get(url)                    - Get raw HTML from URL
rhtml.browse(url)                 - Open URL in browser
rhtml.browseget(url)              - Browse and get HTML
rhtml.openjs(filename)            - Run JavaScript file
rhtml.openhtml(filename)          - Open HTML file in browser

-- RAUDIO --
raudio.play(filename, async_play) - Play audio file
raudio.stop()                     - Stop playing audio
raudio.beep(frequency, duration)  - Play system beep
raudio.play_system_sound(name)    - Play Windows system sound

-- RMOUSE --
rmouse.mouse(position, click, double) - Control mouse
rmouse.position()                     - Get mouse position
rmouse.scroll(clicks, direction)      - Scroll mouse wheel

-- USAGE EXAMPLES --
>>> from reader import rfiles, rhtml, raudio
>>> rfiles.create("hello.txt", "Hello, World!")
>>> rhtml.browse("github.com")
>>> raudio.play("explosion.wav")

-- VERSION --
1.0.0

from . import rfiles
from . import rhtml
from . import raudio
from . import rmouse

__version__ = "1.0.0"
__author__ = "StarShot Studios"
__all__ = ['rfiles', 'rhtml', 'raudio', 'rmouse']