# READER: rfiles
"""
rfiles.py - File and process operations module
Part of the reader library
developed by StarShot Studios
"""

import os
import subprocess
import signal
import sys

def run(program):
    """
    Run a file as if double-clicked (opens with default application)
    
    Args:
        program (str): Path to the file or program
        
    Returns:
        subprocess.Popen or None: The process object (Unix) or None (Windows)
    """
    try:
        if sys.platform == "win32":
            # Windows: os.startfile acts like double-clicking
            os.startfile(program)
            return None
        elif sys.platform == "darwin":
            # macOS: use 'open' command (like double-clicking in Finder)
            subprocess.Popen(["open", program])
            return None
        else:
            # Linux: use 'xdg-open' (like double-clicking in file manager)
            subprocess.Popen(["xdg-open", program])
            return None
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{program}' not found")
    except Exception as e:
        raise Exception(f"Failed to run '{program}': {str(e)}")

def stop(program_name):
    """
    Stop a running program by name
    
    Args:
        program_name (str): Name of the program to stop (e.g., 'minecraft.exe' or 'minecraft')
        
    Note:
        This uses OS-specific commands. Requires appropriate permissions.
    """
    try:
        if sys.platform == "win32":
            # Windows: use taskkill
            subprocess.run(["taskkill", "/F", "/IM", program_name], 
                         check=True, 
                         capture_output=True)
        else:
            # Unix-like: use pkill
            subprocess.run(["pkill", "-f", program_name], 
                         check=True, 
                         capture_output=True)
    except subprocess.CalledProcessError:
        raise Exception(f"Failed to stop '{program_name}'. Process may not be running or insufficient permissions.")
    except Exception as e:
        raise Exception(f"Error stopping '{program_name}': {str(e)}")


def create(filename, content=""):
    """
    Create a new file with optional content
    
    Args:
        filename (str): Name/path of the file to create
        content (str): Content to write to the file (default: empty string)
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        raise Exception(f"Failed to create '{filename}': {str(e)}")


def read(filename):
    """
    Read and return the contents of a file
    
    Args:
        filename (str): Name/path of the file to read
        
    Returns:
        str: Contents of the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except Exception as e:
        raise Exception(f"Failed to read '{filename}': {str(e)}")


def write(filename, content):
    """
    Write content to a file (overwrites existing content)
    
    Args:
        filename (str): Name/path of the file to write to
        content (str): Content to write to the file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        raise Exception(f"Failed to write to '{filename}': {str(e)}")


def delete(filename):
    """
    Delete a file
    
    Args:
        filename (str): Name/path of the file to delete
    """
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except PermissionError:
        raise PermissionError(f"Permission denied to delete '{filename}'")
    except Exception as e:
        raise Exception(f"Failed to delete '{filename}': {str(e)}")


# Additional utility functions that might be useful:

def exists(filename):
    """
    Check if a file exists
    
    Args:
        filename (str): Name/path of the file to check
        
    Returns:
        bool: True if file exists, False otherwise
    """
    return os.path.exists(filename)


def append(filename, content):
    """
    Append content to a file
    
    Args:
        filename (str): Name/path of the file to append to
        content (str): Content to append to the file
    """
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        raise Exception(f"Failed to append to '{filename}': {str(e)}")
