@echo off


@echo off

REM Get information about the Windows operating system
for /f "tokens=2 delims=:" %%a in ('systeminfo ^| find "OS Name"') do set osname=%%a
for /f "tokens=2 delims=:" %%a in ('systeminfo ^| find "OS Version"') do set osversion=%%a

REM Determine the edition of Windows
if "%osname%" == "Microsoft Windows 10 Home" (
    set osedition=Home
) else if "%osname%" == "Microsoft Windows 10 Pro" (
    set osedition=Pro
) else if "%osname%" == "Microsoft Windows Server 2019 Standard" (
    set osedition=Standard
) else if "%osname%" == "Microsoft Windows Server 2019 Datacenter" (
    set osedition=Datacenter
) else (
    echo Unknown Windows edition: %osname%
    goto end
)

REM Enable Hyper-V based on the edition of Windows
if "%osedition%" == "Home" (
    echo Hyper-V is not supported on Windows 10 Home.
) else if "%osversion%" == "10.0.17763" (
    powershell.exe -Command "Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All"
) else if "%osversion%" == "10.0.18362" (
    powershell.exe -Command "Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All"
) else if "%osversion%" == "10.0.19041" (
    powershell.exe -Command "Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All"
) else if "%osversion%" == "10.0.22000" (
    powershell.exe -Command "Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All"
) else (
    echo Unknown Windows version: %osversion%
)

:end


REM Get the path to the ISO file for the operating system from the user
set /p ISO_PATH=Enter the path to the ISO file for the operating system: 

REM Get the name of the virtual machine from the user
set /p VM_NAME=Enter the name of the virtual machine: 

REM Get the amount of memory (in MB) to allocate to the virtual machine from the user
set /p MEMORY=Enter the amount of memory (in MB) to allocate to the virtual machine: 

REM Get the number of virtual processors to allocate to the virtual machine from the user
set /p VIRTUAL_PROCESSORS=Enter the number of virtual processors to allocate to the virtual machine: 

REM Get the path to the virtual hard disk for the virtual machine from the user
set /p VHDX_PATH=Enter the path to the virtual hard disk for the virtual machine: 

REM Create the virtual machine
echo Creating virtual machine...
powershell.exe -Command "New-VM -Name %VM_NAME% -MemoryStartupBytes %MEMORY% -BootDevice CD -Path C:\Hyper-V"

REM Add a virtual hard disk to the virtual machine
echo Adding virtual hard disk...
powershell.exe -Command "Add-VMHardDiskDrive -VMName %VM_NAME% -Path %VHDX_PATH%"

REM Attach the ISO file to the virtual machine
echo Attaching ISO file...
powershell.exe -Command "Add-VMDvdDrive -VMName %VM_NAME% -Path %ISO_PATH%"

REM Start the virtual machine and wait for it to boot from the ISO file
echo Starting virtual machine...
powershell.exe -Command "Start-VM %VM_NAME%"
timeout /t 60

REM Install the operating system on the virtual machine
echo Installing operating system...
powershell.exe -Command "Get-VM %VM_NAME% | Get-VMDvdDrive | Set-VMDvdDrive -Path $null"
powershell.exe -Command "Get-VM %VM_NAME% | Set-VM -BootOrder @(1,2)"
timeout /t 5
powershell.exe -Command "Get-VM %VM_NAME% | Get-VMDvdDrive | Set-VMDvdDrive -Path %ISO_PATH%"
timeout /t 5

REM Shutdown the virtual machine
echo Shutting down virtual machine...
powershell.exe -Command "Stop-VM %VM_NAME%"

echo Done.
