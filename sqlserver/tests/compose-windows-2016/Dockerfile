# hello
#FROM mcr.microsoft.com/windows/servercore:ltsc2022

#FROM mcr.microsoft.com/windows/servercore:ltsc2022-amd64
FROM mcr.microsoft.com/windows/servercore:ltsc2019

RUN curl https://go.microsoft.com/fwlink/?LinkID=799011 -o SQLServer2016-SSEI-Eval.exe
RUN .\SQLServer2016-SSEI-Eval.exe /ACTION="install" /IACCEPTSQLSERVERLICENSETERMS /QUIET /VERBOSE /TCPENABLED:1

COPY sqlserver-initial-setup.ps1 sqlserver-initial-setup.ps1
RUN powershell -F .\sqlserver-initial-setup.ps1

CMD ping -t localhost > NUL
