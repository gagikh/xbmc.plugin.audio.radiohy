
# returns the current sorted list of known stations
import operator

# TODO: verify stations
#{
#    "Name":"HayFM",
#    "Url":"http://hayfm.am:8000/",
#    "Icon":""
#},

#cityfm, http://www.cityfm.am/
#radio alpha
#Armenian Radio NJ (weekly show Sun 2-4 PM on WSOU 89.5 FM): https://armenianradionj.net/
#radiomayak
#"Name":     "Lounge Radio Yerevan",
#"http://www.acabc.ca/radio-show"

# crontab TIME format: 
# MIN HOUR DOM MON DOW CMD - "* * * * *"

def getStations(sortingKey):
    resp = [

    	   {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "Kegham Depoyan",
                "Email":    "info@radioarev.com",
                "Icon":     "https://www.radioarev.com/images/radioarev.png",
                "Name":     "Radio Arev",
                "Phone":    "+961-3-466270",
                "Schedule": "* * * * *",
                "Url":      "https://cast6.asurahosting.com/proxy/radioare/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radioarev.com"
                },
    	   {
                "Address":  "Beirut",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "yeridasartoutiantsayne@gmail.com",
                "Icon":     "https://cdn-profiles.tunein.com/s186962/images/logod.png?t=637037958650000000",
                "Name":     "Yeridasartoutyan Tsayny",
                "Phone":    "+961 76 464343",
                "Schedule": "* * * * *",
                "Url":      "http://65.108.98.93:8123/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://yeridasartoutiantsayne.com/"
                },
    	   {
                "Address":  "0052 Nairi Zaryan str 22a, Yerevan, Armenia",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "radioaurora@radioaurora.am",
                "Icon":     "https://radioaurora.am/ui/img/logo.png",
                "Name":     "Radio Aurora",
                "Phone":    "+37410 251007",
                "Schedule": "* * * * *",
                "Url":      "https://de.auroramedia.am/aurora.mp3",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radioaurora.am"
                },
            {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "radioayk@gmail.com",
                "Icon":     "https://static.wixstatic.com/media/b1dfa3_be9e61c7b63b9cafdaa5275c3285ca55.png",
                "Name":     "Radio AYK",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://64.150.176.42:8117/;listen.mp3",
                "Verified": "false",
                "Video":    "false",
                "WebPage":  "http://www.radioayk.com"
                },
            {
                # verified
                "Address":  "0025 Yerevan, Alex Manoogian 5 str",
                "Country":  "Armenia",
                "Director": "Armen Amiryan",
                "Email":    "aa@arradio.am",
                "Icon":     "https://cdn-profiles.tunein.com/s347439/images/logog.png?t=1",
                "Name":     "Yerevan FM",
                "Phone":    "+374-10-55-11-43",
                "Schedule": "* * * * *",
                "Url":      "https://eu1.stream4cast.com/proxy/arradioi/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.yerevanfm.am/"
                },
            {
                "Address":  "405 Waltham St. Lexington, MA 02421-7954",
                "Country":  "USA",
                "Director": "",
                "Email":    "info@bashde.org",
                "Icon":     "https://cdn.onlineradiobox.com/img/logo/5/43015.v2.png",
                "Name":     "Armenian Christian Radio",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "https://streams.radio.co/sa0bf8ec29/listen",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://bashde.org"
                },
            {
                "Address":  "Yerevan, Qochar 21",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "impulse@impulse.am",
                "Icon":     "https://www.lratvakan.am/media/company/logo/corporate-logo_IAoQCpL.png",
                "Name":     "Lratvakan Radio",
                "Phone":    "+374 60 37 12 73",
                "Schedule": "* * * * *",
                "Url":      "http://212.34.233.78:8000/live",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.lratvakan.am/"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "info@lavradio.am",
                "Icon":     "http://www.lavradio.am/wp-content/uploads/2017/02/logo-1.png",
                "Name":     "Energy FM",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "https://eu.stream4cast.com/proxy/energyfm/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.lavradio.am"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "info@lavradio.am",
                "Icon":     "http://www.lavradio.am/wp-content/uploads/2017/02/logo-1.png",
                "Name":     "XFM Radio",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "https://eu.stream4cast.com/proxy/xfmradio/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.lavradio.am"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "info@lavradio.am",
                "Icon":     "http://www.lavradio.am/wp-content/uploads/2017/02/logo-1.png",
                "Name":     "MFM Music Radio",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "https://eu.stream4cast.com/proxy/mfmradio/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.lavradio.am"
                },
            { # verified!
                "Address":  "",
                "Country":  "Armenia",
                "Director": "Aghabek Margaryan",
                "Email":    "info@lavradio.am",
                "Icon":     "http://www.lavradio.am/wp-content/uploads/2017/02/logo-1.png",
                "Name":     "Lav Radio Mix",
                "Phone":    "+37455830003",
                "Schedule": "* * * * *",
                "Url":      "https://eu.stream4cast.com/proxy/lavradiomix/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.lavradio.am"
                },
            { # verified!
                "Address":  "",
                "Country":  "Armenia",
                "Director": "Aghabek Margaryan",
                "Email":    "info@lavradio.am",
                "Icon":     "http://www.lavradio.am/wp-content/uploads/2017/02/logo-1.png",
                "Name":     "Lav Radio",
                "Phone":    "+37455830003",
                "Schedule": "* * * * *",
                "Url":      "https://eu.stream4cast.com/proxy/lavradio/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.lavradio.am"
                },
            {
                "Address":  "",
                "Country":  "Turkey",
                "Director": "",
                "Email":    "info@norradyo.com",
                "Icon":     "http://www.ermenikultur.org/wp-content/uploads/2013/10/Nor_Radyo__g_rsel.jpg",
                "Name":     "Nor Radyo",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://norradyo.com:8000/live",
                "Verified": "false",
                "Video":    "false",
                "WebPage":  "http://www.norradyo.com"
                },
            {
                # verified!
                "Address":  "Yerevan 25, Aleq Manukyan 5",
                "Country":  "Armenia",
                "Director": "Armen Amiryan",
                "Email":    "aa@arradio.am",
                "Icon":     "http://www.armradio.am/hy/wp-content/uploads/2014/10/logo_hy.png",
                "Name":     "Public Radio of Armenia",
                "Phone":    "+374-10-55-11-43",
                "Schedule": "* * * * *",
                "Url":      "https://eu1.stream4cast.com/proxy/publicra/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.armradio.am"
                },
            {
                "Address":  "4 rue Marcellin Berthelot 69150 DECINES",
                "Country":  "France",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.radioarmenie.com/images/logo-long.png",
                "Name":     "Radio Armenie",
                "Phone":    "04-78-49-52-74",
                "Schedule": "* * * * *",
                "Url":      "http://direct.radioarmenie.com:9029/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radioarmenie.com"
                },
            {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "info@radioavol.org",
                "Icon":     "http://www.arm-radio.com/wp-content/uploads/2016/07/radio-avol.png",
                "Name":     "Radio AVOL",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://199.189.111.28:8209/stream",
                "Verified": "false",
                "Video":    "false",
                "WebPage":  "http://radioavol.org"
                },
            {
                "Address":  "41 rue des ecolses, 94140 Alfortville",
                "Country":  "France",
                "Director": "",
                "Email":    "",
                "Icon":     "https://radio-aypfm.com/assets/img/logo-header.png",
                "Name":     "Radio AYP",
                "Phone":    "01-43-53-19-90",
                "Schedule": "* * * * *",
                "Url":      "http://stric6.streamakaci.com/radioayp.mp3",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://radio-aypfm.com"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "",
                "Icon":     "http://radiohay.am/wp-content/uploads/2018/12/Logo-urish-chapi.png",
                "Name":     "Radio Hay (Yerevan)",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://16242.cloudrad.io:9178/live",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://radiohay.am"
                },
            {
                "Address":  "",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "info@radiojan.am",
                "Icon":     "http://www.radiojan.am/images/logo2new.png",
                "Name":     "Radio Jan",
                "Phone":    "+374-96-01-08-55",
                "Schedule": "* * * * *",
                "Url":      "http://s7.voscast.com:10258/radiojan",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.radiojan.am"
                },
            {
                "Address":  "Beirut, Khatchadurian Street, Khederlarian Building, Ground Floor",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "",
                "Icon":     "http://www.radiosevan.com/resources/radiosevan/css/images/logo.png",
                "Name":     "Radio Sevan",
                "Phone":    "+961-1-567161/2/3",
                "Schedule": "* * * * *",
                "Url":      "http://sevan.bitwize.me:8018",
                "Verified": "false",
                "Video":    "false",
                "WebPage":  "http://www.radiosevan.com"
                },
            {
                "Address":  "",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "",
                "Icon":     "http://static.wixstatic.com/media/9badce_2edb315888ac483287408d2d6d0d3d48.jpg_srz_p_171_87_75_22_0.50_1.20_0.00_jpg_srz",
                "Name":     "Radio Spyurq",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://manager1.creativradio.pro:2690/stream",
                "Verified": "false",
                "Video":    "false",
                "WebPage":  "http://www.radiospurk.com"
                },
            {
                "Address":  "Yerevan, Xandjyan 13a",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "radiovan@radiovan.am",
                "Icon":     "https://www.radiovan.fm/css/images/radiovan.svg",
                "Name":     "Radio Van",
                "Phone":    "+374-10-54-00-01",
                "Schedule": "* * * * *",
                "Url":      "http://stream.radiovan.fm/stream/index.m3u8",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://radiovan.am"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "radioyan@imarmenian.com",
                "Icon":     "http://www.haykakanmusic.com/images/radio-yeraz.jpg",
                "Name":     "Radio Yeraz",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "http://149.255.60.194:8008/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://radioyeraz.com"
                },
            {
                "Address":  "",
                "Country":  "",
                "Director": "",
                "Email":    "",
                "Icon":     "http://triktrak.ca/wp-content/uploads/2015/07/Triktrak_LOGO_small.png",
                "Name":     "Trik Trak",
                "Phone":    "",
                "Schedule": "* * * * *",
                "Url":      "https://cast3.my-control-panel.com/proxy/triktrak/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://triktrak.ca"
                },
            {
                "Address":  "Yerevan, Azatutyun Ave. 1/21",
                "Country":  "Armenia",
                "Director": "",
                "Email":    "info@vem.am",
                "Icon":     "https://vem.am/uploads/images/contents/24e2eedb71bf6569ae0c5e9daf3f7fac.svg",
                "Name":     "Vem Radio",
                "Phone":    "+374-10-54-88-70",
                "Schedule": "* * * * *",
                "Url":      "https://eu1.stream4cast.com/proxy/vemradio/stream",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.vem.am/"
                },
            {
                "Address":  "Center Shaghzoyan, 2nd Floor, Bourj Hammoud, Metn, Lebanon",
                "Country":  "Lebanon",
                "Director": "",
                "Email":    "info@voiceofvan.net",
                "Icon":     "https://www.voiceofvan.net/backend/uploads/setting/1723180428.png",
                "Name":     "Voice of Van",
                "Phone":    "+961-1-241272",
                "Schedule": "* * * * *",
                "Url":      "https://vovan.s3ming.com/vovan.mp3",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.voiceofvan.net/"
                },
            {
                # verified!
                "Address":  "3200 Wilshire Blvd. Ste 902NT, Los Angeles, CA, United States 90010",
                "Country":  "USA",
                "Director": "Sarkis Chakarian",
                "Email":    "info@yerevannights.com",
                "Icon":     "http://www.armenische-kirche.ch/wp-content/uploads/2013/02/yerevannights.jpg",
                "Name":     "Yerevan Nights",
                "Phone":    "+1-877-220-8951",
                "Schedule":"* * * * *",
                "Url":      "http://icecast.worldweb.services:80/Web",
                "Verified": "true",
                "Video":    "false",
                "WebPage":  "http://www.yerevannights.com"
                }
            ]
    if sortingKey not in ("Name", "Country", "Video"):
        sortingKey = "Name"
    resp.sort(key=operator.itemgetter(sortingKey))
    return resp
