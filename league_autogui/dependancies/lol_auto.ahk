#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Start Code
!j::
send #1
WinWait, Windows PowerShell
	; run cmd.exe
    ; WinWait, ahk_exe cmd.exe ; Wait for CMD to start
    ; Send c:{enter} ; Go to C drive
    Send cd C:\Users\ricky\Documents\python_scripts\git_ready\scratch\league_autogui\{enter} ; go to script's folder
    Send python league_auto_oop.py{enter}

; just automatically closes for some reason
; runwait, python C:\Users\ricky\Documents\python_scripts\git_ready\scratch\league_autogui\league_auto_vf.py{enter}