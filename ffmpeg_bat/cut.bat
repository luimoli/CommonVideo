@REM set inputfile = "C:\\Users\\liumm\\Videos\\SZ-video\\sony4K.mxf"
set inputfile = "\\192.168.100.201\MediaStore-share\广电资料\伟大征程（广电真4K片源）.mxf"


set outputfile = "C:\\Users\\liumm\\Videos\\SZ-video\\journey_01.mxf"

@REM ffmpeg -ss <start time> -t <duration> -i <input file> -c:v copy -c:a copy <output file>

@REM ffmpeg -ss 00:43:51.601 -to 00:44:01.038 -i %input_file% -c:v copy -c:a copy %output_file%
ffmpeg -ss 00:52:55.676 -to 00:53:02.761 -i "\\192.168.100.201\MediaStore-share\广电资料\伟大征程（广电真4K片源）.mxf" -c:v copy -c:a copy "C:\\Users\\liumm\\Videos\\SZ-video\\journey_02.mxf"


ffmpeg -ss 01:40:48.000 -to 01:40:50.000 -i "\\192.168.100.201\MediaStore-share\广电资料\伟大征程（广电真4K片源）.mxf" -c:v copy -c:a copy "C:\\Users\\liumm\\Videos\\SZ-video\\journey_05.mxf"

00:33:33.362
00:33:37.362

pause

