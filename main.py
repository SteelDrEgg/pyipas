import argparse, subprocess
import os
from getinfo import *
from genplist import *

#生成传参
parser = argparse.ArgumentParser(prog='ipa utility',description='by iOS Archive')

#type是要传入的参数的数据类型  help是该参数的提示信息
# parser.add_argument('p', help='generate plist', action='store_true')
# parser.add_argument('i', help='get ipa info', action='store_true')
# nargs='+'

parser.add_argument('app', type=str, help='[p] generate plist, [i] get ipa info') #Choose app
parser.add_argument('-i', type=str, help='absolute ipa path') #Ipa path
parser.add_argument('-o', type=str, help='Output path', default=os.path.abspath(os.getcwd())) #Output path
# parser.add_argument('-bi', type=str,nargs='+', help='ipa bundle infos, such as arch, BundleIdentifier') #bundle infos
parser.add_argument('-iu', type=str, help='.ipa url (only necessary when generating plist') #ipa url
parser.add_argument('-fi', type=str, help='plist full size icon, unnecessary') #full size icon
parser.add_argument('-di', type=str, help='plist diaplay icon, unnecessary') #display icon
parser.add_argument('-an', type=str, help='plist app name, unnecessary') #plist install title
parser.add_argument('-st', type=str, help='plist subtitle, unnecessary') #plist install subtitle

args = parser.parse_args()

if args.app=='p':
    print('plist')
elif args.app=='i':
    print("info")
else:
    print("inavailable args")