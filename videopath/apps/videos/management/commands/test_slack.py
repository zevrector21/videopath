from django.core.management.base import BaseCommand
from videopath.apps.videos.models import Video

IDS = ["WDsLAmcYdZMlGdKh","FqCE0143","mxGDfzvy","EEpp6gdK","NH7yAjsP","5mFGKnft","s8PMJDGg","Nv9NeigN","rJi07QWw","Q7pvpt3C","R3vAm5mh","mfWvosrQ","jyUPeCVz","b87SicVP","c24mXxN8","TzMZEAmy","rasMLzqC","zu3qfV1F","bizPJyVS","naWCNANy","Z9qoTLRz","jv5Nq8MG","D0r9gpqJ","7vvVUqnO","E3fPEGbB","PrPO6yVX","6Y6tLJGZ","FWKL3bWa","rRk8fvt5","FC5iWNcw","msqDChXP","7KMLlcbQ","cxp0U1QN","G7E7yxAj","1uQCBIW9","Gq6IiVgo","IiXZplHV","sPNwgLja","2CYEuCLk","I7BhoZ1A","lfNv5INx","yURYG2Q4","wTGUd0Im","QojuRIOa","VSVlR5FL","BnZ6hH2l","9HFvUeQp","4jJyQetc","tcwUqmLc","baY0ZSPV","q9IjIOyp","wOzvsN4J","4SlvS20j","dK0v7g0h","HTSXK9su","UoqgnQP3","7QLbwUzw","1EgmhF5T","cBEWd928","U8QyYj1U","7MccKCBT","Q1eus5sf","SpnJZDbd","4YTrtULp","kogTmMJG","9DJHIg8N","yQChi6kb","Q7tgr0kg","QhR093xa","SJqScXDV","kIZR3bHg","koXY9cH5","yuCdybOn","phxi199C","CWF7LTIl","a2boFb3l","m0etmDX9","GRK0Y7DM","LX2lYH2r","3wYs1w2w","X9KmEqlW","eiIhT8cC","19jSpcg5","2LLB63Ly","AjXaoXbl","jVBSDQFW","vnNUV50J","u9ENCes4","8ao3JDSO","V0JeNzti","hpCwKk5y","pWWats3p","FqCE0143","WDsLAmcYdZMlGdKh","z67zHvRX","nnVXZhKt","y0pciZv1","8dYIxeQC"]

class Command(BaseCommand):
    def handle(self, *args, **options):
       	for key in IDS:
       		video = Video.objects.get(key=key)
       		video.export_jpg_sequence()

	
