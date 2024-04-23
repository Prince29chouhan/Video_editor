from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx, CompositeAudioClip

clip1 = VideoFileClip("video_sample2.mp4").subclip(1,5).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip2 = VideoFileClip("video_sample2.mp4").subclip(30,40).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip3 = VideoFileClip("video_sample2.mp4").subclip(84,90).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip4= VideoFileClip("video_sample2.mp4").subclip(113,131).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip5 = VideoFileClip("video_sample2.mp4").subclip(144,146).fx(vfx.fadein, 1).fx(vfx.fadeout, 1).rotate(180)
clip6 = VideoFileClip("video_sample2.mp4").subclip(146,150).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)


audio = AudioFileClip("audio_sample2.mp3").subclip(1,45).fx(afx.audio_fadein, 1)


combined = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5, clip6])
combined.audio = CompositeAudioClip([audio])

combined.write_videofile("final_video.mp4")