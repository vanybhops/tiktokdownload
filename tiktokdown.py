from requests_html import HTMLSession
import requests,re
headers={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "sec-gpc": "1",
}
session = requests.Session()
session.get('https://www.tiktok.com',headers=headers)
def linkdown(x):
    ses=HTMLSession()
    r=ses.get(x)
    reg=re.compile(r'(?<=\[{"url":")(.*?)(?=",)')
    response=ses.get(reg.search(r.html.html)[0].replace(r"\u002F",r"/"))
    f=open(x.split("/")[3].replace("@","")+".mp4",'wb');
    for chunk in response.iter_content(chunk_size=255):
        if chunk:
            f.write(chunk)
    f.close()
    print("downloaded :{}.mp4".format(x.split("/")[3].replace("@","")))
def search(x):
    response=session.get(f"https://m.tiktok.com/api/search/general/full/?browser_language=en-US&is_page_visible=true&keyword={x}",headers=headers)
    response=requests.get(response.json()["data"][0]["item"]["video"]["downloadAddr"],headers=headers)
    f=open(x+".mp4",'wb');
    for chunk in response.iter_content(chunk_size=255):
        if chunk:
            f.write(chunk)
    f.close()
    print("downloaded :{}.mp4".format(x))

while True:
    yinput=str(input("input a name or a link: "))
    if "https://"in yinput:
        linkdown(yinput)
    else:
        search(yinput)
