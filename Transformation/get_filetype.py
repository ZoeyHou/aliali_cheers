import magic

video_type_tuple = ('ISO Media, MP4 Base Media v1 [IS0 14496-12:2003]',
                    'Macromedia Flash Video')

image_type_tuple = ('JPEG', 'PNG', 'BMP', 'GIF')

audio_type_tuple = ('Audio file with ID3 version 2.3.0',
                    'RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, stereo 44100 Hz',
                    'Audio file with ID3 version 2.4.0, contains: MPEG ADTS, layer III, v1,  64 kbps, 44.1 kHz, Stereo')


def get_pictype(file):
    return magic.from_file(file).split(' ')[0]

def get_videotype(video):
    return magic.from_file(video)

def get_audiotype(audio):
    return magic.from_file(audio)
