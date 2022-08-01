import os
from moviepy.editor import VideoFileClip
import pathlib
import urllib.request
import requests


# You are working on a project for TikTok.
# The future project will be a web-site of all public GIF images.
# You need to write a function that converts TikTok video to GIF.
# The input parameter is url address of TikTok video,
# i.e. "TikTok example". The output parameter is path to GIF image,
# i.e. "/home/user/TikTok-example-1.gif".
# https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55

def convert_to_gif():
    url = input("Enter the Tik-Tok-url\n")
    # url = "https://v16-webapp.tiktok.com/e0a122756ee01a539819be618b31a859/62e87744/video/tos/useast2a/tos-useast2a-pve-0068/6c5970b2c4c746c39e17748d12516a80/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2170&bt=1085&btag=80000&cs=0&ds=3&ft=gKSYZ8kuo0PD18~N4sg9wKX2O5LiaQ2D~t8&mime_type=video_mp4&qs=0&rc=ZTs1OGhoNjtnPDxnOTY5OEBpamZrOTg6ZnZkZDMzNzczM0AyYGFiM2JeNTMxYzMxNmM1YSNpX19wcjRfX2BgLS1kMTZzcw%3D%3D&l=2022080119000001019017602127570120"
    response = requests.get(url, allow_redirects=True)
    name = input("Enter the name for the future gif\n")
    gif_name = name + ".gif"
    with open("tiktok_video_downloaded.mp4", "wb+") as out_file:
        out_file.write(response.content)
    tik_tok_video = VideoFileClip("tiktok_video_downloaded.mp4")
    tik_tok_video.write_gif(gif_name, fps=1, program='ffmpeg')
    print(os.getcwd() + "/" + gif_name)


convert_to_gif()
