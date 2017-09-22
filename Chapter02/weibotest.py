from weibo import APIClient

APP_KEY = '3488205433' # app key
APP_SECRET = 'f652c1e4238a28d2d2d03a6d95ba5a16' # app secret
CALLBACK_URL = 'http://baageer.io' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print(url)

code='32a859bad6e20be791d41b716c4c715b'
r = client.request_access_token(code)
access_token = r.access_token # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
# TODO: 在此可保存access token
client.set_access_token(access_token, expires_in)

print (client.statuses.user_timeline.get())
