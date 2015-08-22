import weibo
APP_KEY='849896661'
APP_SECRET='eb4e401711a6559719713f560c029601'
CALL_BACK='https://api.weibo.com/oauth2/default.html'
def SinaAuth():
    client=weibo.APIClient(APP_KEY,APP_SECRET,CALL_BACK)
    auth_url=client.get_authorize_url()
    print("auth_url:"+auth_url)
    code=raw_input("input the returned code:")
    r=client.request_access_token(code)
    client.set_access_token(r.access_token,r.expires_in)

    while True:
        print ("ready! Do you want to send a new weibo?(y/n)")
        choice=raw_input()
        if choice=='y' or choice=='Y':
                content=raw_input('input the you new weibo content:')
                if content:
                        client.statuses.update.post(status=content)
                        print('send successfully!')
                        break
                else:
                        print('error! empty content')
        if choice=='n' or choice=='N':
                 break
if __name__=='__main__':
        SinaAuth()


