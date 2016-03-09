@ECHO off

IF EXIST %SYSTEMROOT%\py.exe (
    CMD /k py.exe -3.5 bot.py
    EXIT
)
