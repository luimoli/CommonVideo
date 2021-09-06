@REM set image_path1="F:\POC\20210721_zhongguang\video1_420p_hdr_denoiselaparY\%%7d.png"
set image_path1="C:\Users\liumm\Videos\SZ-video\sony4K_01\%%7d.png"

@REM set video_path1="F:\POC\20210721_zhongguang\video1_420p_hdr_denoiselaparY.ts"
set video_path1="C:\Users\liumm\Videos\SZ-video\sony4K_01.mxf"

ffmpeg -i %video_path1% -filter_complex "scale=in_color_matrix=bt2020" %image_path1%
pause