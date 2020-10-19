# Install Choco
Open PowerShell as administrator  
Run the following command

```PowerShell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```
**Note:** This will setuup PowerShell execution policy and install chocolatey

# VSCode
```PowerShell
choco install vscode --version 1.50.0 --params "/NoDesktopIcon" 
choco install vscode-ansible
choco install vscode-python
```

Alternatively you can download the installer from: https://code.visualstudio.com/Download

# Install Vagrant
```PowerShell
choco install vagrant --version 2.2.10
``` 

Alternavletly you can download and install it from: 
https://releases.hashicorp.com/vagrant/2.2.10/vagrant_2.2.10_x86_64.msi

# Vagrant and Hyper-v
Vagrant comes with support out of the box for Hyper-V, a native hypervisor written by Microsoft. However, Hyper-V must be enabled prior to using the provider.

```PowerShell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

# Docker Desktop
choco install docker-desktop
