import zipfile, plistlib, re, os, stat, subprocess

def analyze_ipa_with_plistlib(ipa_file):
    plist_path = find_plist_path(ipa_file)
    plist_data = ipa_file.read(plist_path)
    plist_root = plistlib.loads(plist_data)
    return plist_root

def find_plist_path(zip_file):
    name_list = zip_file.namelist()
    pt=r'Payload'+os.sep+'[^'+os.sep+']*.app'+os.sep+'Info.plist'
    # pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
    pattern = re.compile(pt)
    for path in name_list:
        m = pattern.match(path)
        if m is not None:
            return m.group()

# def print_ipa_info(plist_root):
#     class binfo:
#         name=''
#         osl=''
#         ver=''
#         bid=''
#
#     bundle=binfo()
#     bundle.osl=plist_root['MinimumOSVersion']
#     # str(int(os.stat('%s'%(ipa_path)).st_size / (1024 * 1024)))+'M'
#     bundle.ver='V'+plist_root['CFBundleVersion']
#     bundle.bid=plist_root['CFBundleIdentifier']
#     try:
#         bundle.name=plist_root['CFBundleName']
#     except Exception:
#         bundle.name=plist_root['CFBundleDisplayName']
#     # bundle.aid=plist_root['AppID']
#     return bundle

def extract_exe(ipa,proot,wd):
    exe = ''
    for file in ipa.namelist():
        if proot['CFBundleExecutable'] == file.split(os.sep)[-1]:
            exe = file
            break
    ipa.extract(path=wd + '/temp', member=exe)
    return wd+'/temp/'+exe

def analyze_exe(exe):
    #Determine encrypt
    zj=''
    cmd = subprocess.run(['otool', '-l', exe], stdout=subprocess.PIPE, shell=False, cwd=None, encoding='utf-8')
    cor=cmd.stdout.find('cryptid')
    jz=cmd.stdout[cor+8]
    if jz=='1':
        zj='ZB'
    else:
        zj='JB'

    #Determine 32-bits or 64-bits
    arc=''
    def deter(arci):
        if str(cmd.stdout).find(str(arci)) !=-1:
            return True
        else:
            return False

    #Get architecture
    cmd = subprocess.run(['lipo', '-info', exe], stdout=subprocess.PIPE, shell=False, cwd=None, encoding='utf-8')

    #Analyze architecture
    if deter('v7') and deter('64'):
        arc='32&64'
    elif deter('v6') or deter('v7'):
        arc='32'
    elif deter('64') or deter('v8'):
        arc='64'

    return zj,arc


def getinfo(path):
    wd=os.path.abspath(os.getcwd())
    ipa = zipfile.ZipFile(path)
    proot = analyze_ipa_with_plistlib(ipa)
    try:
        os.makedirs(wd+'/temp',mode=0o777)
    except Exception:
        print('Error making directory')
    exe=extract_exe(ipa,proot,wd)
    bunInfo=analyze_exe(exe)
    zj=bunInfo[0]
    arc=bunInfo[1]
    out={}

    # return analyze_ipa_with_plistlib(path)