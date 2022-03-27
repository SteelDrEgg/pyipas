def genp(data):
    plist='''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>items</key>
    <array>
        <dict>
            <key>assets</key>
            <array>
                <dict>
                    <key>kind</key>
                    <string>software-package</string>
                    <key>url</key>
                    <string>{ipaUrl}</string>
                </dict>
                <dict>'''.format(ipaUrl=data.ipaUrl)
    if data['fullIcon'] !=None:
        plist=plist+'''
                <dict>
                    <key>kind</key>
                    <string>full-size-image</string>
                    <key>needs-shine</key>
                    <false/>
                    <key>url</key>
                    <string>%s</string>
                </dict>'''%data['fullIcon']

        if data['disIcon']!=None:
            plist=plist+'''
                <dict>
                    <key>kind</key>
                    <string>display-image</string>
                    <key>needs-shine</key>
                    <false/>
                    <key>url</key>
                    <string>%s</string>
                </dict>'''%data['disIcon']

        plist=plist+'''
            </array>
            <key>metadata</key>
            <dict>
                <key>bundle-identifier</key>
                <string>{bid}</string>
                <key>bundle-version</key>
                <string>1.0</string>
                <key>kind</key>
                <string>software</string>'''.format(bid=data['bundleId'])

        if data['subTitle']!=None:
            plist=plist+'''
                <key>subtitle</key>
                <string>%s</string>'''%data['subTitle']

        plist=plist+'''
                <key>title</key>
                <string>%s</string>
            </dict>
        </dict>
    </array>
</dict>
</plist>'''%data['title']

        return plist
