
----- mac os ------

добовление для текщего пользователя

cd $home
nano ~/.bash_profile
PATH=$PATH:/путь_папка/к/команде

Добавление для всех пользователей

sudo nano /etc/paths
PATH=$PATH:/путь_папка/к/команде

----- linux ------

sudo vi /etc/environment # ubuntu

 /etc/profile


----- windows ------

Для одного
setx path "%PATH%;C:\путь\к\директории\"

для всех 

C:\> setx /M path "%PATH%;C:\путь\к\директории\"