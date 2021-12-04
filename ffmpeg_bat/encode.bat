@REM set image_path1="F:\POC\20210713_shenzMetro\1_clip\%%7d.bmp"
@REM set output_path1="F:\POC\20210713_shenzMetro\1_clip.mp4"

@REM set image_path2="F:\POC\20210713_shenzMetro\2_clip\%%7d.bmp"
@REM set output_path2="F:\POC\20210713_shenzMetro\2_clip.mp4"

@REM ffmpeg -r 30.00 -i %image_path1% -vcodec libx264   -crf 0 -pix_fmt yuv444p  %output_path1%
@REM ffmpeg -r 25.00 -i %image_path2% -vcodec libx264   -crf 0 -pix_fmt yuv444p  %output_path2%
@REM pause


@REM -------------------------------------------------------------------------------------------------

set image_path="C:\Users\liumm\Videos\SZ-video-img\journey_02_sdr\%%7d.png"
set output_path="C:\Users\liumm\Videos\SZ-video-img\journey_02_sdr_n.mp4"

@REM ffmpeg -r 50.00 -i %image_path1% -vcodec libx264   -crf 0 -pix_fmt yuv444p  %output_path1%

@REM ffmpeg -r <fps> -i <input images patten> -vf "scale=in_color_matrix=bt709" -c:v libx264 -x264-params colorprim=bt709:transfer=bt709:colormatrix=bt709 -crf 10 -pix_fmt yuv420p <output file>

ffmpeg -r 50.00 -i %image_path% -vcodec libx264 -vf "scale=in_color_matrix=bt709"  -v warning -crf 10 -color_range 1 -colorspace bt709 -color_primaries bt709 -color_trc bt709 %output_path%

@REM ffmpeg -r 50.00 -i %image_path% -vf "scale=in_color_matrix=bt709" -c:v libx264 -x264-params colorprim=bt709:transfer=bt709:colormatrix=bt709 -crf 10 -pix_fmt yuv420p %output_path%

pause
