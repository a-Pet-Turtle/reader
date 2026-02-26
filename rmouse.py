# READER: rmouse
"""
rmouse.py - Mouse controller
Part of the reader library
developed by StarShot Studios

NOTE: Mouse control is NOT available in Python's built-in libraries.
This module uses ctypes to interface with OS-level APIs as a workaround.
For better cross-platform support, use third-party library: pyautogui

WARNING: This is platform-specific and may not work in all environments.
"""

import sys
import ctypes
import time


if sys.platform == "win32":
    # Windows API constants
    MOUSEEVENTF_MOVE = 0x0001
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004
    MOUSEEVENTF_RIGHTDOWN = 0x0008
    MOUSEEVENTF_RIGHTUP = 0x0010
    MOUSEEVENTF_MIDDLEDOWN = 0x0020
    MOUSEEVENTF_MIDDLEUP = 0x0040
    MOUSEEVENTF_ABSOLUTE = 0x8000


def mouse(position=None, click=None, double=False):
    """
    Control mouse position and clicks
    
    Args:
        position (tuple): (x, y) coordinates to move to (optional)
        click (str): 'left', 'right', or 'middle' to click (optional)
        double (bool): If True, perform double-click (default False)
        
    Examples:
        mouse(position=(100, 200))  # Move to (100, 200)
        mouse(click='left')  # Left click at current position
        mouse(position=(500, 300), click='right')  # Move and right-click
        mouse(click='left', double=True)  # Double-click at current position
    """
    if sys.platform == "win32":
        _mouse_windows(position, click, double)
    elif sys.platform == "darwin":
        _mouse_macos(position, click, double)
    else:
        _mouse_linux(position, click, double)


def _mouse_windows(position, click, double):
    """Windows implementation using ctypes and Win32 API"""
    try:
        # Move mouse if position specified
        if position is not None:
            x, y = position
            ctypes.windll.user32.SetCursorPos(x, y)
        
        # Perform click if specified
        if click:
            click = click.lower()
            
            if click == 'left':
                ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                
                if double:
                    time.sleep(0.05)
                    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    
            elif click == 'right':
                ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                
                if double:
                    time.sleep(0.05)
                    ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                    ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                    
            elif click == 'middle':
                ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
                ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
                
                if double:
                    time.sleep(0.05)
                    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
                    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
            else:
                raise ValueError(f"Invalid click type: '{click}'. Use 'left', 'right', or 'middle'.")
                
    except Exception as e:
        raise Exception(f"Mouse operation failed: {str(e)}")


def _mouse_macos(position, click, double):
    """macOS implementation using AppleScript"""
    import subprocess
    
    try:
        if position is not None:
            x, y = position
            # Use cliclick if available, otherwise limited functionality
            script = f'tell application "System Events" to set position of mouse to {{{x}, {y}}}'
            subprocess.run(["osascript", "-e", script], check=True)
        
        if click:
            click = click.lower()
            click_count = 2 if double else 1
            
            # This is very limited - macOS doesn't allow easy mouse clicks via AppleScript
            # User would need to install cliclick or other tools
            raise NotImplementedError(
                "Mouse clicking on macOS requires third-party tools (cliclick, pyautogui). "
                "Install with: brew install cliclick"
            )
            
    except Exception as e:
        raise Exception(f"Mouse operation failed on macOS: {str(e)}")


def _mouse_linux(position, click, double):
    """Linux implementation using xdotool"""
    import subprocess
    
    try:
        if position is not None:
            x, y = position
            subprocess.run(["xdotool", "mousemove", str(x), str(y)], check=True)
        
        if click:
            click = click.lower()
            click_num = {'left': '1', 'middle': '2', 'right': '3'}.get(click)
            
            if not click_num:
                raise ValueError(f"Invalid click type: '{click}'. Use 'left', 'right', or 'middle'.")
            
            if double:
                subprocess.run(["xdotool", "click", "--repeat", "2", click_num], check=True)
            else:
                subprocess.run(["xdotool", "click", click_num], check=True)
                
    except FileNotFoundError:
        raise Exception(
            "xdotool not found. Install with: sudo apt-get install xdotool"
        )
    except Exception as e:
        raise Exception(f"Mouse operation failed on Linux: {str(e)}")


def position():
    """
    Get current mouse position
    
    Returns:
        tuple: (x, y) coordinates of mouse cursor
    """
    if sys.platform == "win32":
        # Windows
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
        
        pt = POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
        return (pt.x, pt.y)
        
    elif sys.platform == "darwin":
        # macOS - limited without third-party tools
        raise NotImplementedError(
            "Getting mouse position on macOS requires third-party libraries (pyautogui)."
        )
        
    else:
        # Linux with xdotool
        import subprocess
        try:
            result = subprocess.run(
                ["xdotool", "getmouselocation", "--shell"],
                capture_output=True,
                text=True,
                check=True
            )
            lines = result.stdout.strip().split('\n')
            x = int(lines[0].split('=')[1])
            y = int(lines[1].split('=')[1])
            return (x, y)
        except:
            raise Exception("xdotool not found. Install with: sudo apt-get install xdotool")


def scroll(clicks, direction='down'):
    """
    Scroll the mouse wheel
    
    Args:
        clicks (int): Number of scroll clicks
        direction (str): 'up' or 'down' (default 'down')
    """
    if sys.platform == "win32":
        # Windows scrolling
        MOUSEEVENTF_WHEEL = 0x0800
        WHEEL_DELTA = 120
        
        amount = WHEEL_DELTA * clicks
        if direction.lower() == 'down':
            amount = -amount
            
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, amount, 0)
        
    else:
        raise NotImplementedError(
            "Scrolling on macOS/Linux requires third-party libraries (pyautogui) "
            "or system tools (xdotool on Linux)."
        )
