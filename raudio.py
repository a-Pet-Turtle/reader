# READER: raudio
"""
raudio.py - Audio controller
Part of the reader library
developed by StarShot Studios

NOTE: Built-in audio support is very limited in Python.
- Windows: Can play WAV files with winsound
- macOS/Linux: Can use OS commands to play audio
- For MP3/other formats, requires third-party libraries (pygame, playsound, etc.)
"""

import sys
import os
import subprocess

if sys.platform == "win32":
    import winsound


def play(filename, async_play=False):
    """
    Play an audio file
    
    Args:
        filename (str): Path to audio file
        async_play (bool): If True, play asynchronously (non-blocking). Windows WAV only.
        
    Note:
        - Windows: Only supports WAV files natively
        - macOS/Linux: Uses system commands, supports various formats
        - For MP3 support on Windows, use third-party libraries
    """
    try:
        if sys.platform == "win32":
            # Windows - only WAV files supported with built-in winsound
            if filename.lower().endswith('.wav'):
                flags = winsound.SND_FILENAME
                if async_play:
                    flags |= winsound.SND_ASYNC
                else:
                    flags |= winsound.SND_SYNC
                winsound.PlaySound(filename, flags)
            else:
                # Try to open with default program for other formats
                os.startfile(filename)
                
        elif sys.platform == "darwin":
            # macOS - use afplay command
            if async_play:
                subprocess.Popen(["afplay", filename])
            else:
                subprocess.run(["afplay", filename])
                
        else:
            # Linux - try multiple players
            players = ["aplay", "paplay", "ffplay", "mpg123", "play"]
            for player in players:
                try:
                    if async_play:
                        subprocess.Popen([player, filename], 
                                       stdout=subprocess.DEVNULL, 
                                       stderr=subprocess.DEVNULL)
                    else:
                        subprocess.run([player, filename],
                                     stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL,
                                     check=True)
                    break
                except (FileNotFoundError, subprocess.CalledProcessError):
                    continue
            else:
                # Fallback: open with default application
                subprocess.Popen(["xdg-open", filename])
                
    except Exception as e:
        raise Exception(f"Failed to play '{filename}': {str(e)}")


def stop():
    """
    Stop currently playing audio
    
    Note:
        This is very limited with built-in libraries.
        Only works reliably on Windows for WAV files played with winsound.
    """
    if sys.platform == "win32":
        try:
            winsound.PlaySound(None, winsound.SND_PURGE)
        except:
            pass
    else:
        # On Unix systems, try to kill common audio players
        # This is a crude approach and may not work reliably
        players = ["afplay", "aplay", "paplay", "ffplay", "mpg123", "play"]
        for player in players:
            try:
                subprocess.run(["pkill", player], 
                             stdout=subprocess.DEVNULL, 
                             stderr=subprocess.DEVNULL)
            except:
                pass


def beep(frequency=1000, duration=500):
    """
    Play a system beep sound
    
    Args:
        frequency (int): Frequency in Hz (Windows only, default 1000)
        duration (int): Duration in milliseconds (Windows only, default 500)
        
    Note:
        - Windows: Can generate beeps at specific frequencies
        - macOS/Linux: Plays default system beep (ignores frequency/duration)
    """
    try:
        if sys.platform == "win32":
            winsound.Beep(frequency, duration)
        elif sys.platform == "darwin":
            # macOS - system beep
            os.system("afplay /System/Library/Sounds/Ping.aiff")
        else:
            # Linux - terminal bell
            print("\a", end="", flush=True)
    except Exception as e:
        # Fallback to simple bell
        print("\a", end="", flush=True)


def play_system_sound(sound_name):
    """
    Play a Windows system sound by name
    
    Args:
        sound_name (str): System sound name (e.g., 'SystemAsterisk', 'SystemExclamation')
        
    Note: Windows only. Common sounds:
        - SystemAsterisk
        - SystemExclamation  
        - SystemExit
        - SystemHand
        - SystemQuestion
    """
    if sys.platform == "win32":
        try:
            winsound.PlaySound(sound_name, winsound.SND_ALIAS | winsound.SND_ASYNC)
        except:
            raise Exception(f"Failed to play system sound '{sound_name}'")
    else:
        raise NotImplementedError("System sounds only available on Windows")


# Microphone input is not possible with built-in libraries
# Would require: pyaudio, sounddevice, or similar third-party library
def record():
    """
    Record audio from microphone
    
    Note: NOT AVAILABLE with built-in libraries.
    Requires third-party library like pyaudio or sounddevice.
    """
    raise NotImplementedError(
        "Audio recording requires third-party libraries (pyaudio, sounddevice). "
        "Not available with built-in Python libraries."
    )
