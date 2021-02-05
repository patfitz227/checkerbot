import requests
from bs4 import BeautifulSoup as soup

headers = { # taken from scrapehero https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
        }


sites= {
    'walmartSeriesX':{
        'name':'Walmart series x standard edition',
        'url': 'https://www.walmart.com/ip/XB1-Xbox-Series-X/443574645?irgwc=1&sourceid=imp_zyUWXj3DaxyLTxrwUx0Mo389UkEWUgVxRVILUQ0&veh=aff&wmlspartner=imp_159047&clickid=zyUWXj3DaxyLTxrwUx0Mo389UkEWUgVxRVILUQ0&sharedid=cnet&affiliates_ad_id=565706&campaign_id=9383',
        'check':'<div class="prod-blitz-copy-message">This item is <b>out of stock</b>.</div>',
        'search': 'prod-blitz-copy-message' 
        },
    'gamestopSeriesX':{
        'name':'Gamestop series x standard edition',
        'url': 'https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x/B224744V.html',
        'check':'''<div class="option-card-footer">
<span class="delivery-home-stock-msg"></span>
<span class="delivery-out-of-stock text-uppercase hide">Out of Stock</span>
<span class="delivery-unavailable text-uppercase hide">unavailable</span>
</div>''',
        'search': 'option-card-footer'
        },
    'neweggSeriesX':{
        'name':'Newegg series x standard edition',
        'url': 'https://www.newegg.com/p/68-105-273?nm_mc=AFC-RAN-COM&cm_mmc=AFC-RAN-COM&utm_medium=affiliates&utm_source=afc-CNET&AFFID=8003&AFFNAME=CNET&ACRID=1&ASUBID=cn-e99561079ac74850947dd034a1ec4bc9-dtp&ASID=https%3A%2F%2Fwww.cnet.com%2F&ranMID=44583&ranEAID=8003&ranSiteID=0JlRymcP1YU-JqanzEmtk8T7JkHm.cY.OA',
        'check':'<div class="product-inventory"><strong><i class="fas fa-exclamation-triangle"></i> OUT OF STOCK.</strong></div>',
        'search': 'product-inventory' 
        },
    'walmartSeriesXAccess':{
        'name':'Walmart series x Access bundle',
        'url': 'https://www.walmart.com/cp/xbox-all-access/8571041',
        'check':'''<div class="cta btn-text-static" style="border-color: rgb(127, 127, 127); border-radius: 4px; background-color: rgb(127, 127, 127); border-width: 2px; color: rgb(255, 255, 255);">Coming Soon</div>''',
        'search': 'cta btn-text-static'
        },
    'gamestopSeriesXAccess':{
        'name':'Gamestop series x Acess bundle',
        'url': 'https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x-xbox-all-access/B224744A.html',
                'check':'''<div class="option-card-footer">
<span class="delivery-home-stock-msg"></span>
<span class="delivery-out-of-stock text-uppercase hide">Out of Stock</span>
<span class="delivery-unavailable text-uppercase hide">unavailable</span>
</div>''',
        'search': 'option-card-footer'
        }
}




for key in sites.keys():
    walmart= requests.get(sites[key]['url'], headers=headers)
    soupyness = soup(walmart.content, 'html.parser')
    check = str(soupyness.find('div', attrs={'class':sites[key]['search']}))
    if check == sites[key]['check']:
        print(sites[key]['name'], 'Status hasnt changed')
    else:
        print(sites[key]['name'], 'Status has changed',sites[key]['url'])

#https://www.tomsguide.com/news/where-to-buy-xbox-series-x-stock

