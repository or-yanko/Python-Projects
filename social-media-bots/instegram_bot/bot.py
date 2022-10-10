from instapy import InstaPy
from instapy import smart_run














usrname = input('enter your username: ')
psswrd = input('enter your password: ')

#usrname = 'papinho231'
#psswrd = 'aaa123456'

print(usrname,psswrd)

try:
    session  = InstaPy(username=usrname, password=psswrd, headless_browser=True)

    with smart_run(session):
        #session.set_relationship_bounds(enabled=True,delimit_by_numbers=True,max_followers=500,min_followers=30,min_following=50)

        session.follow_by_list(['oryanko'])
        while True:
            cmd = input('@',usrname, '  bot teminal migaaaa ;-)\n---->\t')
            if cmd.lower() == '':
                print("""followers
                following
                not following back => nfb""")
            elif cmd.lower() == 'followers':
                print('\tyour followers:')
                for f in session.grab_followers():
                    print('# ', f)
                print('\n')
            elif cmd.lower() == 'followering':
                print('\tyour following:')
                for f in session.grab_following():
                    print('# ', f)
                print('\n')
            elif cmd.lower() == 'nfu':
                print('\tyour followers:')
                followers = session.grab_followers()
                following = session.grab_following()
                for f in following:
                    if f not in followers:
                        print('# ', f)
                print('\n')

except:
    print('wromg username or password')
