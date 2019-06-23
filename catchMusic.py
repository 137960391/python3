import requests
import re
guid = '3094068815'
headers = {
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
song_name = '张韶涵'
html_data = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&qqmusic_ver=1298&new_json=1&p=1&n=8&aggr=1&w=' + song_name).text
music_data = re.findall('action.*?"name":"(.*?)","subtitle.*?"grp".*?language.*?mid":"(.*?)","mv.*?singer.*?name":"(.*?)","title.*?time_public":"(.*?)","title":"(.*?)","title_hilight.*?"ver":0,"volume', html_data , re.S)

for music_list in music_data:
    music_album , music_songmid , music_author , music_time , music_name = music_list
    data = '&data={"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"' + guid +'","songmid":["'+ music_songmid +'"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'
    music_url_data = requests.get('https://u.y.qq.com/cgi-bin/musicu.fcg?', data)
    music_url = re.findall('purl":"(.*?)","qmdlfromtag', music_url_data.text ,re.S)
    print ('  歌曲名: ' + music_name + '  歌手: ' + music_author + ' 专辑：' + music_album + ' 歌曲时间：' + music_time)
    print ('  歌曲链接：' + ' http://dl.stream.qqmusic.qq.com/' + music_url[0])
    #    print (music , album , author , time , 'https://y.qq.com/n/yqq/song/'+ mid + '.html')
