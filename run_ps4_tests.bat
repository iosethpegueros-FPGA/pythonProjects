@echo off

echo this program should run ps1 python example from MIT fall 2022

REM conda activate 

cd mit6_100l_f22_ps4_code/1_ps4

echo printing directory 
echo %cd%
REM conda init cmd.exe


REM call C:\ProgramData\anaconda3\Scripts\activate.bat

REM python ps4c.py
REM pause

echo **********
echo **********
echo **********
echo running Tests on ps4a
echo **********
python test_ps4a_student.py


echo **********
echo **********
echo **********
echo running Tests on ps4c
echo **********
python test_ps4bc_student.py

cd ..\..\
