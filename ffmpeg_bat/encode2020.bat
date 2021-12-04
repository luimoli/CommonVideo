@REM set image_path1="F:\POC\20210721_zhongguang\video1_420p_hdr_deblock_sr\%%7d.png"
@REM set output_path1="F:\POC\20210721_zhongguang\video1_420p_hdr_deblock_sr.mp4"
@REM ffmpeg -r 25.00 -i %image_path1% -vcodec libx264 -vf "scale=in_color_matrix=bt2020"  -crf 5 -color_range 1 -colorspace bt2020nc -color_primaries bt2020 -color_trc arib-std-b67  %output_path1%


set image_path1="C:\Users\liumm\Videos\SZ-video\honggaoliang_hdr400_v2\%%7d.png"
set output_path1="C:\Users\liumm\Videos\SZ-video\honggaoliang_hdr400_v2.mp4"

ffmpeg -r 25.00 -i %image_path1% -vcodec  libx264 -vf "scale=in_color_matrix=bt2020"  -v warning -crf 0 -color_range 1 -colorspace bt2020nc -color_primaries bt2020 -color_trc arib-std-b67  %output_path1%

pause