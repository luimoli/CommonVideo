import imageio_ffmpeg
import os
import numpy as np
import torch


class InferVideo:
    def __init__(self, read_pix_fmt_in='rgb24', bits_per_pixel=24, 
                        write_pix_fmt_in='rgb24',write_pix_fmt_out='yuv420p'):
        self.read_pix_fmt_in = read_pix_fmt_in
        self.bits_per_pixel = bits_per_pixel
        self.read_output_params=['-filter_complex', 'scale=in_color_matrix=bt709:in_range=limited']
        # self.read_output_params=['-filter_complex', 'scale=in_color_matrix=smpte170m:in_range=limited']

        self.write_pix_fmt_in = write_pix_fmt_in
        self.write_pix_fmt_out = write_pix_fmt_out
        self.write_input_params = ['-filter_complex', 'scale=in_color_matrix=bt709:out_color_matrix=bt709']
        self.write_output_params = ['-x264-params', 'colorprim=bt709:transfer=bt709:colormatrix=bt709']
        # self.write_input_params = ['-filter_complex', 'scale=in_color_matrix=smpte170m:out_color_matrix=smpte170m:in_range=limited:out_range=limited']
        # self.write_output_params = ['-x264-params', 'colorprim=bt470bg:transfer=bt470bg:colormatrix=bt470bg']
    
        self.dtype = np.uint8


    def forward(self, src_video_path, dst_video_dir, dst_videoname_suffix):
        """[summary]

        Args:
            src_video_path ([str]): [Input video's path]
            dst_video_dir ([str]): [Output video's saving folder]
            dst_videoname_suffix ([str]): [the output video's name = input_video_name + dst_videoname_suffix]
        """
        in_reader = imageio_ffmpeg.read_frames(src_video_path, 
                                                pix_fmt=self.read_pix_fmt_in, 
                                                bits_per_pixel=self.bits_per_pixel,
                                               output_params=self.read_output_params)
        meta = in_reader.__next__()
        fps, size = meta['fps'], meta['size']
        src_video_name = os.path.basename(src_video_path).split('.')[0]
        dst_video_path = os.path.join(dst_video_dir, f'{src_video_name}_{dst_videoname_suffix}.mp4')

        out_writer = imageio_ffmpeg.write_frames(dst_video_path, 
                                                 size=size,
                                                 pix_fmt_in=self.write_pix_fmt_in,
                                                 pix_fmt_out=self.write_pix_fmt_out,
                                                 fps=fps,
                                                 macro_block_size=1, 
                                                 quality=10,
                                                 input_params=self.write_input_params,
                                                 output_params=self.write_output_params,
                                                 codec='libx264')
        out_writer.send(None)

        for frame_idx, frame_buffer in enumerate(in_reader):
            frame = np.frombuffer(frame_buffer, dtype=self.dtype).reshape(size[1], size[0], 3)

            # frame = (frame / 255).astype(np.float32)
            # image_rgb_hwc = torch.from_numpy(frame)
            # frame_tensor = self.HDRConvention.sdr_to_hdr(image_rgb_hwc)
            # out_frame = frame_tensor.cpu().numpy() * 65535
            # out_frame = out_frame.clip(0, 65535).astype(np.uint16)

            out_writer.send(frame)
            print('frame {} has done!'.format(frame_idx + 1))

        out_writer.close()


if __name__ == '__main__':

    # save_path = r'C:\temp\hdr_v8_test'
    # pix_fmt_in = 'rgb24'
    # bits_per_pixel = 24
    # pix_fmt_out = 'yuv422p10le'

    # videos_path = r'C:\temp\sdr_video'

    # videos = sorted(os.listdir(videos_path))
    # for video in videos:
    #     # for video in ['10BaoFeng-1min.mxf']:  # 'hgl.mxf',
    #     #     for i in [60, 70, 80, 90, 100]:
    #     infer = InferVideo(pix_fmt_in=pix_fmt_in, bits_per_pixel=bits_per_pixel, pix_fmt_out=pix_fmt_out,
    #                        save_dir=save_path, skin_point=(45, 86), high_light=(100, 260))
    #     video_path = os.path.join(videos_path, video)
    #     infer.forward(video_path)
    
    
    infer = InferVideo()
    src_video_path = r'C:\Users\liumm\Videos\aaavideo\smore.mov'
    dst_video_dir = r'C:\Users\liumm\Videos\aaavideo\\'
    dst_videoname_suffix = 'test'
    infer.forward(src_video_path=src_video_path, dst_video_dir=dst_video_dir, dst_videoname_suffix=dst_videoname_suffix)
