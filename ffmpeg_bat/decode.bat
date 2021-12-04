@REM set video_path="temp.MXF"
@REM set image_path="bt709_ffmpeg_xmf2png/%%5d.png"
@REM ffmpeg -i %video_path% %image_path%


@REM ffmpeg -i temp.mxf -c:v rawvideo -vframes 100 -pix_fmt yuv422p temp.yuv
@REM ffmpeg -i 3WenNuan-1min.mxf -c:v rawvideo -pix_fmt yuv444p out444.yuv

@REM ffplay -video_size 1920x1080 -i out.yuv

@REM ffmpeg -s 1920x1080 -pix_fmt yuv422p -i 00001.yuv  out.png
@REM pause

@REM ffmpeg -i out.yuv -c:v rawvideo -pix_fmt yuv422p out.mxf

@REM ffmpeg -s 1920x1080 -pix_fmt yuv422p -i out.yuv %image_path%

ffmpeg -i HongGaoLiang-3min.mxf -filter_complex "scale=in_color_matrix=bt709:in_range=limited" ./sdr_images/%%5d.png
ffmpeg -i HongGaoLiang-3min_high_300_alpha_400.mp4 -filter_complex "scale=in_color_matrix=bt2020:in_range=limited" ./hdr_images/%%5d.png


@REM in_color_matrix decide the output type
@REM ffmpeg -i _5min_p_HLG_denoise.MP4 -vframes 10 -filter_complex "scale=in_color_matrix=bt2020" HGL/%%5d.png
@REM ffmpeg -i temp.MXF -vframes 100 -filter_complex "scale=in_color_matrix=bt601" w_matrix_coefficient709_filter_complex_in601/%%5d.png
@REM ffmpeg -i temp.MXF -vframes 100 -filter_complex "scale=in_color_matrix=bt709" w_matrix_coefficient709_filter_complex_in709/%%5d.png
@REM ffmpeg -i temp.MXF -vframes 100 -filter_complex "scale=in_color_matrix=bt601:in_range=limited" w_matrix_coefficient709_filter_complex_in601_inlimit/%%5d.png
@REM ffmpeg -i temp.MXF -vframes 100 -filter_complex "scale=in_color_matrix=bt601:in_range=full" w_matrix_coefficient709_filter_complex_in601_infull/%%5d.png
@REM ffmpeg -i temp.MXF -vframes 100 -filter_complex "scale=in_color_matrix=bt709" w_matrix_coefficient709_filter_complex_in709/%%5d.png


@REM ffmpeg -i temp.MXF -vframes 100 -filter_complex "scale=in_color_matrix=bt601:out_color_matrix=bt601" w_matrix_coefficient709_filter_complex_in601_out601/%%5d.png
@REM ffmpeg -i temp.MXF -vframes 100 -filter_complex "scale=in_color_matrix=bt601:out_color_matrix=bt709" w_matrix_coefficient709_filter_complex_in601_out709/%%5d.png
@REM ffmpeg -i temp.MXF -vframes 100 -filter_complex "scale=in_color_matrix=bt709:out_color_matrix=bt601" w_matrix_coefficient709_filter_complex_in709_out601/%%5d.png
@REM ffmpeg -i temp.MXF -vframes 100 -filter_complex "scale=in_color_matrix=bt709:out_color_matrix=bt709" w_matrix_coefficient709_filter_complex_in709_out709/%%5d.png

@REM ffmpeg -i news_210709_ditfnet_H264_Part1_59to70-or-84to100.mp4 -filter_complex "scale=in_color_matrix=bt709:in_range=limited" news1/%%5d.png
@REM ffmpeg -i news_210709_ditfnet_H264_Part2_68to100-or-55to100.mp4 -filter_complex "scale=in_color_matrix=bt709:in_range=limited" news2/%%5d.png
@REM ffmpeg -i news_210709_ditfnet_H264_Part3_33to70-or-67to100.mp4 -filter_complex "scale=in_color_matrix=bt709:in_range=limited" news3/%%5d.png

@REM ffmpeg  -start_number 0 -r 25 -i news1_results/%%5d.png -vf "scale=in_color_matrix=bt709" -b:v 3600k -c:v libx264 -x264-params colorprim=bt709:transfer=bt709:colormatrix=bt709 -crf 0 -pix_fmt yuv420p news1_results.mp4
@REM ffmpeg  -start_number 0 -r 25 -i news3_results67_100/%%5d.png -vf "scale=in_color_matrix=bt709" -b:v 2500k -c:v libx264 -x264-params colorprim=bt709:transfer=bt709:colormatrix=bt709 -crf 0 -pix_fmt yuv420p news3_results.mp4
@REM ffmpeg  -start_number 0 -r 25 -i news2_results_55_100/%%5d.png -vf "scale=in_color_matrix=bt709" -b:v 3000k -c:v libx264 -x264-params colorprim=bt709:transfer=bt709:colormatrix=bt709 -crf 0 -pix_fmt yuv420p news2_results.mp4
@REM ffmpeg  -start_number 0 -r 25 -i final_results/%%5d.png -vf "scale=in_color_matrix=bt709" -b:v 3000k -c:v libx264 -x264-params colorprim=bt709:transfer=bt709:colormatrix=bt709 -crf 0 -pix_fmt yuv420p final_results.mp4

@REM pause
@REM ffmpeg -s 1920x1080 -i 00001.yuv -pix_fmt yuv422p10be 00001_10.yuv


@REM  ffmpeg -i 201407_yadif_720p_diernet_hdr_1.mp4 -filter_complex "scale=in_color_matrix=bt709:in_range=limited" ./temp/video1_yadif_hdr_images_1/%%5d.png
@REM  ffmpeg -i 201407_yadif_720p_diernet_hdr_2.mp4 -filter_complex "scale=in_color_matrix=bt709:in_range=limited" ./temp/video1_yadif_hdr_images_2/%%5d.png
@REM  ffmpeg -i 201407_yadif_720p_diernet_hdr_3.mp4 -filter_complex "scale=in_color_matrix=bt709:in_range=limited" ./temp/video1_yadif_hdr_images_3/%%5d.png
@REM  ffmpeg -i 201407_yadif_720p_diernet_hdr_4.mp4 -filter_complex "scale=in_color_matrix=bt709:in_range=limited" ./temp/video1_yadif_hdr_images_4/%%5d.png
@REM  ffmpeg -i 201407_yadif_720p_diernet_hdr_5.mp4 -filter_complex "scale=in_color_matrix=bt709:in_range=limited" ./temp/video1_yadif_hdr_images_5/%%5d.png
@REM  ffmpeg -i 201407_yadif_720p_diernet_hdr_6.mp4 -filter_complex "scale=in_color_matrix=bt709:in_range=limited" ./temp/video1_yadif_hdr_images_6/%%5d.png


@REM ffmpeg -ss 16 -t 2 -i ./right.mp4 -c:v copy -c:a copy ./right_2s.mp4
@REM  ffmpeg -i right_2s.mp4 -c:v rawvideo -pix_fmt yuv422p10le temp.yuv
@REM  ffmpeg -f concat -i ./temp/filelist.txt -c copy output.mp4


@REM  ffmpeg -i 201407.mp4 -vn -c:a copy 201407_audio.mp3
@REM  ffmpeg -i 201407.mp4 -vn -codec copy 201407_audio.m4a
@REM ffmpeg  -i 201407.mp4 -i 201407_audio.m4a -c:v copy -c:a copy -strict experimental 201407_withAudio.mp4
pause



