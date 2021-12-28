# hello
#FROM mcr.microsoft.com/windows/servercore:ltsc2022

#FROM mcr.microsoft.com/windows/servercore:ltsc2022-amd64
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# download sql-server 2019
RUN curl https://go.microsoft.com/fwlink/?linkid=866662 -o SQL2019-SSEI-Dev.exe
#RUN .\SQL2019-SSEI-Dev.exe /ACTION="install" /IACCEPTSQLSERVERLICENSETERMS /QUIET /VERBOSE /TCPENABLED:1

COPY sqlserver-initial-setup.ps1 sqlserver-initial-setup.ps1
#RUN powershell -F .\sqlserver-initial-setup.ps1

#CMD ping -t localhost > NUL
