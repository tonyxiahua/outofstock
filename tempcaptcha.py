import subprocess
import config
import win32clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(config.amazon_url +"\n\n" + config.newegg_url)
win32clipboard.CloseClipboard()
subprocess.call(['C:\\Program Files\\AutoHotkey\\AutoHotkey.exe',"callme.ahk"])
