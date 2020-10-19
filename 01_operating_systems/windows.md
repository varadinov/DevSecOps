# Command Lets (cmdlets)
A PowerShell cmdlet is a lightweight command that is used in the Windows PowerShell environment. Cmdlet follow a **Verb-Noun ** naming standard such as Start-Process.
```
Get-Verb - The Get-Verb function gets verbs that are approved for use in PowerShell commands.
```

```
PowerShell common verbs
- New- Creates a new resource 
- Set- Modifies an existing resource
- Get- Retrieves an existing resource
- Read- Gets information from a source, such as a file
- Find- Used to look for an object 
- Search- Used to create a reference to aresource 
- Start- (asynchronous) begin an operation, such as starting a process
- Invoke- (synchronous) perform an operation such as running a command
```

# Get Help
```PowerShell
Get-Help <cmdlet> - Read cmdlet documentation
Get-Help <cmdlet> -online - Read online documentation
Get-Command - list of all available cmdlets
Get-Command –Verb Set - list all available cmdlets with verb **Set**
Get-Command –Noun process - list all cmdlets with noun **process**
```

# File Management
```PowerShell
Get-ChildItem
Copy-Item src.txt dst.txt 
Move-Item src.txt dst.txt 
Select-String –path *.txt –pattern <password>
Get-Content file.txt
Get-Location
```

# Process Management
```PowerShell
Get-Process 
Get-Process   
Start-Process 
Stop-Process  
Wait-Process  
```

# Service Management
```PowerShell
Get-Service 
Restart-Service 
Start-Service   
Stop-Service    
```

# Converting Formats
```PowerShell
Get-Process | ConvertTo-Json
Get-Process | ConvertTo-Csv
```

# Navigate the Windows registry
```PowerShell
cd HKLM:\ 
```
**Note:** you can navigate using the same set of commands used for file system navigation

# Set Executioin policy
PowerShell by default cannot execute unsiged scripts. This is configured for security reasons. If you want to execute unsigned scripts, you can change this configuration. 
```
Set-Executionpolicy RemoteSigned
```
