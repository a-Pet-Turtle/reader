# ── ANSI text formatting ───────────────────────────────────────────────────────
R  = "\033[0m"   # reset all
B  = "\033[1m"   # bold
DM = "\033[2m"   # dim
IT = "\033[3m"   # italic
UL = "\033[4m"   # underline
BL = "\033[5m"   # blink

# foreground colours
BLACK   = "\033[30m"; GREY    = "\033[90m"
RED     = "\033[31m"; LRED    = "\033[91m"
GREEN   = "\033[32m"; LGREEN  = "\033[92m"
YELLOW  = "\033[33m"; LYELLOW = "\033[93m"
BLUE    = "\033[34m"; LBLUE   = "\033[94m"
MAGENTA = "\033[35m"; LMAGENTA= "\033[95m"
CYAN    = "\033[36m"; LCYAN   = "\033[96m"
WHITE   = "\033[37m"; LWHITE  = "\033[97m"

# background colours
BG_BLACK   = "\033[40m";  BG_GREY    = "\033[100m"
BG_RED     = "\033[41m";  BG_LRED    = "\033[101m"
BG_GREEN   = "\033[42m";  BG_LGREEN  = "\033[102m"
BG_YELLOW  = "\033[43m";  BG_LYELLOW = "\033[103m"
BG_BLUE    = "\033[44m";  BG_LBLUE   = "\033[104m"
BG_MAGENTA = "\033[45m";  BG_LMAGENTA= "\033[105m"
BG_CYAN    = "\033[46m";  BG_LCYAN   = "\033[106m"
BG_WHITE   = "\033[47m";  BG_LWHITE  = "\033[107m"

# ── Cursor control ─────────────────────────────────────────────────────────────
def pos(row, col):
    """Move cursor to row, col (1-indexed, top-left is 1,1)"""
    return f"\033[{row};{col}H"

def move_up(n=1):    return f"\033[{n}A"
def move_down(n=1):  return f"\033[{n}B"
def move_right(n=1): return f"\033[{n}C"
def move_left(n=1):  return f"\033[{n}D"

CLEAR_SCREEN = "\033[2J"    # clear entire screen
CLEAR_LINE   = "\033[2K"    # clear current line
HOME         = "\033[H"     # move cursor to top-left
HIDE_CURSOR  = "\033[?25l"  # hide cursor
SHOW_CURSOR  = "\033[?25h"  # show cursor

# ── Helper ─────────────────────────────────────────────────────────────────────
def style(*codes):
    """Combine any styles/colours: style(B, IT, CYAN) -> bold italic cyan"""
    return "".join(codes)

# ── Example ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(CLEAR_SCREEN + HOME)
    print(pos(1, 1) + style(B, UL, LCYAN) + "DUMBBOT INTERFACE" + R)
    print(pos(3, 1) + style(IT, GREY) + "a slightly less dumb bot" + R)
    print(pos(5, 1) + style(B, LGREEN) + "You: " + R + "hello")
    print(pos(6, 1) + style(B, LCYAN)  + "Bot: " + R + "Hey there how are you doing.")
    print(pos(8, 1) + style(DM) + "─" * 40 + R)
    print(pos(9, 1) + BG_BLUE + LWHITE + " > " + R + " ", end="", flush=True)
