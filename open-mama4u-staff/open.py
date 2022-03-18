import webbrowser
from termcolor import colored

lst = [
    'https://mama4u.com/632022-%d7%9b%d7%a4%d7%9b%d7%a4%d7%99-%d7%90%d7%95%d7%a3-%d7%95%d7%95%d7%90%d7%99%d7%98-%d7%97%d7%93%d7%a9%d7%99%d7%9d/#more-806039',
    'https://mama4u.com/16022022-%d7%9b%d7%a4%d7%9b%d7%a4%d7%99-%d7%a0%d7%99%d7%99%d7%a7-%d7%97%d7%93%d7%a9%d7%99%d7%9d/#more-794388',
    'https://mama4u.com/09052020-%d7%9b%d7%a4%d7%9b%d7%a4%d7%99-%d7%a0%d7%99%d7%99%d7%a7-%d7%93%d7%92%d7%9e%d7%99%d7%9d-%d7%97%d7%93%d7%a9%d7%99%d7%9d/#more-406373',
    'https://mama4u.com/1432022-%d7%9e%d7%90%d7%a8%d7%96-5-%d7%91%d7%95%d7%a7%d7%a1%d7%a8%d7%99%d7%9d-%d7%93%d7%99%d7%96%d7%9c/#more-809958',
    'https://mama4u.com/1132022-%d7%97%d7%95%d7%9c%d7%a6%d7%95%d7%aa-%d7%98%d7%99-%d7%90%d7%95%d7%a3-%d7%95%d7%95%d7%90%d7%99%d7%98/#more-808089',
    'https://mama4u.com/1922022-%d7%97%d7%95%d7%9c%d7%a6%d7%95%d7%aa-%d7%98%d7%99-%d7%93%d7%95%d7%9c%d7%a6%d7%94-%d7%92%d7%91%d7%90%d7%a0%d7%94/#more-796693',
    'https://mama4u.com/1632022-%d7%9b%d7%95%d7%91%d7%a2%d7%99-%d7%93%d7%95%d7%9c%d7%a6%d7%94-%d7%92%d7%91%d7%90%d7%a0%d7%94/#more-810797',
    'https://mama4u.com/14122021-%d7%a0%d7%a2%d7%9c%d7%99-%d7%a1%d7%a0%d7%99%d7%a7%d7%a8%d7%a1-%d7%93%d7%95%d7%9c%d7%a6%d7%94-%d7%92%d7%91%d7%90%d7%a0%d7%94/#more-766126',
    'https://mama4u.com/1112022-%d7%a0%d7%a2%d7%9c%d7%99-%d7%a1%d7%a0%d7%99%d7%a7%d7%a8%d7%a1-%d7%93%d7%95%d7%9c%d7%a6%d7%94-%d7%92%d7%91%d7%90%d7%a0%d7%94/#more-782132',
    'https://mama4u.com/11122021-%d7%a0%d7%a2%d7%9c%d7%99-%d7%93%d7%95%d7%9c%d7%a6%d7%94-%d7%92%d7%91%d7%90%d7%a0%d7%94-%d7%97%d7%93%d7%a9%d7%95%d7%aa/#more-763780',
    'https://mama4u.com/1232022-%d7%a0%d7%a2%d7%9c%d7%99-%d7%a1%d7%a0%d7%99%d7%a7%d7%a8%d7%a1-%d7%93%d7%95%d7%9c%d7%a6%d7%94-%d7%92%d7%91%d7%90%d7%a0%d7%94-%d7%91%d7%90%d7%99%d7%9b%d7%95%d7%aa-%d7%9e%d7%a7%d7%95%d7%a8/#more-809005',
    'https://mama4u.com/1922022-%d7%a0%d7%a2%d7%9c%d7%99-%d7%90%d7%a8%d7%9e%d7%90%d7%a0%d7%99-%d7%93%d7%92%d7%9e%d7%99-%d7%90%d7%99%d7%9b%d7%95%d7%aa-%d7%9e%d7%a7%d7%95%d7%a8/#more-797018',
    'https://mama4u.com/1222022-%d7%a9%d7%a2%d7%95%d7%a0%d7%99-%d7%90%d7%a8%d7%9e%d7%90%d7%a0%d7%99/#more-792061',
    'https://mama4u.com/06012022-%d7%a9%d7%a2%d7%95%d7%a0%d7%99-%d7%90%d7%a8%d7%9e%d7%90%d7%a0%d7%99/#more-779522'
]

for url in lst:
    webbrowser.open(url)
    print(colored(url+' has been opened successfully !!!\n\n', 'green'))


