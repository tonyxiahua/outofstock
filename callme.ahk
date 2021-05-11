if WinExist("Google Hangouts - Google Chrome")
{
    WinActivate
    Send {F5}
    Sleep, 4000
    SetKeyDelay, 250
    Send {tab 13}
    Send {return}
    Sleep, 100
    Send ^v
    Send {return}
    Send {tab 4}
    Send {return}
}
Else
{
    Run https://hangouts.google.com/
    Sleep, 5000
    if WinExist("Google Hangouts - Google Chrome")
    {
        WinActivate
        Sleep, 500
        SetKeyDelay, 250
        Send {tab 13}
        Send {return}
        Sleep, 100
        Send ^v
        Send {return}
        Send {tab 4}
        Send {return}
    }
    Else
    {
        MsgBox, 0,, Hangouts tab did not activate.
        FileAppend, %Clipboard%`n, %A_WorkingDir%\Missed Stock\gpu.txt
    }
}
