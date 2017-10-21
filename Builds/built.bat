
pyinstaller --noconfirm ^
    --noconsole ^
    --uac-admin ^
	--distpath %CD%/Builds ^
     %CD%/Builds/build.spec

rmdir /S /Q
 build
Set ZNAME="Builds\LightProgram.zip"

E:\Tools\7-Zip\7z.exe a %ZNAME% "E:\Works\Git\Tools\BatchBuildLightUE4\Builds\Build Light\"

rmdir /S /Q "Builds\Build Light"
