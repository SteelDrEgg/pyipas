import argparse, json
from getinfo import *
from genplist import *

#Generate par
parser = argparse.ArgumentParser(prog='ipa utility',description='by iOS Archive')


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
    json.dumps(getinfo(args.i),open(args.o+'/'+'info.json', 'w'))
elif args.app=='i':
    print('info')
else:
    print("inavailable args")