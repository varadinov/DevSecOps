
# Directory Operations
```
pwd - Show current directory
mkdir dir - Make directory dir
cd dir - Change directory to dir
cd .. - Go up a directory
```

# List files
```
ls - List files
ls -a - Show all (including hidden)
ls -R - Recursive list
ls -r - Reverse order
ls -t - list Sort by last modified
ls -S - Sort by file size
ls -l - Long listing format
ls -1 - list One file per line
ls -m - list Comma-­sep­arated output
```

# Search Files
```
grep <pattern> files - Search for pattern in files
grep -i - Case insens­itive search
grep -r - Recursive search
grep -v - Inverted search
grep -o - Show matched part of file only
find /dir/ -name name* - Find files starting with name in dir
find /dir/ -user name - Find files owned by name in dir
find /dir/ -mmin num - Find files modifed less than num minutes ago in dir
whereis command - Find binary / source / manual for command
locate file - Find file (quick search of system index)
```


# File Operations
```
touch file1 - Create file1
cat file1 file2 - Concat­enate files and output
less file1 - View and paginate file1
file file1 - Get type of file1
cp file1 file2 - Copy file1 to file2
mv file1 file2 - Move file1 to file2
rm file1 - Delete file1
head file1 - Show first 10 lines of file1
tail file1 - Show last 10 lines of file1
tail -F file1 - Output last lines of file1 as it changes
Watch a Command - watch -n 5 'ntpq -p'
```

# File Permissions
```
chown user - changing the ownership of a file/directory
Chown user:group filenam - change the user and group for a file or directory
```

```
PERMISSION      EXAMPLE

U   G   W
rwx rwx rwx     chmod 777 filename
rwx rwx r-x     chmod 775 filename
rwx r-x r-x     chmod 755 filename
rw- rw- r--     chmod 664 filename
rw- r-- r--     chmod 644 filename

LEGEND
U = User
G = Group
W = World

r = Read
w = write
x = execute
- = no access
```

# Process Management
```
ps - Show snapshot of processes
top - Show real time processes
kill pid - Kill process with id pid
pkill name - Kill process with name name
killall name - Kill all processes with names beginning name
program & - Start program in the background
bg - Display stopped or background jobs
fg - brings the most recent background job to foreground
fg n - Brings job n to the foreground
```

# Bash Variables
```
env - Show enviro­nment variables
echo $NAME Output value of $NAME variable
export NAME=value - Set $NAME to value
$PATH - Executable search path
$HOME - Home directory
$SHELL - Current shell
```

# IO Redire­ction
```
cmd < file - Input of cmd from file
cmd1 <(cmd2) - Output of cmd2 as file input to cmd1
cmd > file - Standard output (stdout) of cmd to file
cmd > /dev/null - Discard stdout of cmd
cmd >> file - Append stdout to file
cmd 2> file - Error output (stderr) of cmd to file
cmd 1>&2 - stdout to same place as stderr
cmd 2>&1 - stderr to same place as stdout
cmd &> file - Every output of cmd to file
cmd refers to a command. 
```

# Pipes
```
cmd1 | cmd2 - stdout of cmd1 to cmd2
cmd1 |& cmd2 - stderr of cmd1 to cmd2
```

# Command Lists
```
cmd1 ; cmd2 - Run cmd1 then cmd2
cmd1 && cmd2 - Run cmd2 if cmd1 is successful
cmd1 || cmd2 - Run cmd2 if cmd1 is not successful
```

#  OS Information
```
date - Show system date
uptime - Show uptime
whoami - Show your username
man <command> - Show manual for command
hostname -  Show system host name
w - Display who is online
```

# Bash Shortcuts
```
CTRL-c - Stop current command
CTRL-z - Sleep program
CTRL-r - Search history
!! - Repeat last command
```

# SSH
```
ssh host - Connect to host as your local username.
ssh user@host - Connect to host as user
ssh -p port user@host - Connect to host using port
```

# SSH file transfer
```
scp file.txt server:/tmp - Secure copy file.txt to the /tmp folder on server
scp server:/var/www/*.html /tmp - Copy *.html files from server to the local /tmp folder.
scp -r server:/var/www /tmp - Copy all files and directories recursively from server to the current system's /tmp folder.
```

# Disk Usage
```
df -h - Show free and used space on mounted filesystems
df -i - Show free and used inodes on mounted filesystems
fdisk -l - Display disks partitions sizes and types
du -ah - Display disk usage for all files and directories in human readable format
du -sh - Display total disk usage off the current directory
```

# User and Group Management 
```
id - Display the user and group ids of your current user.
last - Display the last users who have logged onto the system.
who - Show who is logged into the system.
w - Show who is logged in and what they are doing.
groupadd test - Create a group named "test".
useradd -c "John Smith" -m john - Create an account named john, with a comment of "John Smith" and create the user's home directory.
userdel john - Delete the john account.
usermod -aG sales john - Add the john account to the sales group
```

# Hardware Information
```
dmesg - Display messages in kernel ring buffer
cat /proc/cpuinfo - Display CPU information
cat /proc/meminfo - Display memory information
free -h - Display free and used memory ( -h for human readable, -m for MB, -g for GB.)
lspci -tv - Display PCI devices
lsusb -tv - Display USB devices
hdparm -i /dev/sda - Show info about disk sda
```
