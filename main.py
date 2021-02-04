import requests
from bs4 import BeautifulSoup as soup

headers = { # taken from scrapehero https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
        }


sites= {
    'walmart':{
        'url': 'https://www.walmart.com/ip/XB1-Xbox-Series-X/443574645?irgwc=1&sourceid=imp_zyUWXj3DaxyLTxrwUx0Mo389UkEWUgVxRVILUQ0&veh=aff&wmlspartner=imp_159047&clickid=zyUWXj3DaxyLTxrwUx0Mo389UkEWUgVxRVILUQ0&sharedid=cnet&affiliates_ad_id=565706&campaign_id=9383',
        'check':'<div class="prod-blitz-copy-message">This item is <b>out of stock</b>.</div>',
        'search': 'prod-blitz-copy-message' 
        },
    'gamestop':{
        'url': 'https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x/B224744V.html',
        'check':'''<div class="option-card-footer">
<span class="delivery-home-stock-msg"></span>
<span class="delivery-out-of-stock text-uppercase hide">Out of Stock</span>
<span class="delivery-unavailable text-uppercase hide">unavailable</span>
</div>''',
        'search': 'option-card-footer'
        },
    'newegg':{
        'url': 'https://www.newegg.com/p/68-105-273?nm_mc=AFC-RAN-COM&cm_mmc=AFC-RAN-COM&utm_medium=affiliates&utm_source=afc-CNET&AFFID=8003&AFFNAME=CNET&ACRID=1&ASUBID=cn-e99561079ac74850947dd034a1ec4bc9-dtp&ASID=https%3A%2F%2Fwww.cnet.com%2F&ranMID=44583&ranEAID=8003&ranSiteID=0JlRymcP1YU-JqanzEmtk8T7JkHm.cY.OA',
        'check':'<div class="product-inventory"><strong><i class="fas fa-exclamation-triangle"></i> OUT OF STOCK.</strong></div>',
        'search': 'product-inventory' 
        },
    'target':{
        'url': 'https://www.target.com/p/xbox-series-x-console/-/A-80790841?clkid=bd16defeN66f711ebb06342010a246e3d&lnm=81938&',
        'check':'<div class="prod-blitz-copy-message">This item is <b>out of stock</b>.</div>',
        'search': 'prod-blitz-copy-message' 
        },
    'walmartAccess':{
        'url': 'https://www.walmart.com/cp/xbox-all-access/8571041',
        'check':'<div class="prod-blitz-copy-message">This item is <b>out of stock</b>.</div>',
        'search': 'prod-blitz-copy-message' 
        },
    'gamestopAccess':{
        'url': 'https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x-xbox-all-access/B224744A.html',
                'check':'''<div class="option-card-footer">
<span class="delivery-home-stock-msg"></span>
<span class="delivery-out-of-stock text-uppercase hide">Out of Stock</span>
<span class="delivery-unavailable text-uppercase hide">unavailable</span>
</div>''',
        'search': 'option-card-footer'
        }
}




# for key in sites.keys():
#     walmart= requests.get(sites[key]['url'], headers=headers)


#     print(walmart)
walmart= requests.get(sites['target']['url'], headers=headers)
soupyness = soup(walmart.content, 'html.parser')
check = str(soupyness.find('div', attrs={'class':'tyles__BaseWrapper-sc-11r1it6-0 styles__SoldOutWrapper-hphbrb-0 fIHckm gKslGC'}))

print(check)
