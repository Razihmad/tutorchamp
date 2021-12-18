from django.contrib.sitemaps import Sitemap
from django.urls import reverse
        
class Static_Sitemap(Sitemap): 
    static_url_list = [
        {'url':'home','priority':1.0,'changefreq':'daily'},
        {'url':'assignment-help','priority':0.9,'changefreq':'daily'},
        {'url':'feature','priority':0.9,'changefreq':'daily'},
       {'url':'reviews','priority':0.9,'changefreq':'daily'},
       {'url':'about-us','priority':0.9,'changefreq':'daily'},
       {'url':'login','priority':0.9,'changefreq':'daily'},
       {'url':'signup','priority':0.9,'changefreq':'daily'},
       {'url':'tutor','priority':0.9,'changefreq':'daily'},  
       {'url':'registration','priority':0.9,'changefreq':'daily'},
       {'url':'essay','priority':0.9,'changefreq':'daily'},
       {'url':'live','priority':0.9,'changefreq':'daily'},
       {'url':'course-work','priority':0.9,'changefreq':'daily'},
       {'url':'case-study','priority':0.9,'changefreq':'daily'},
       {'url':'dissertation','priority':0.9,'changefreq':'daily'},
       {'url':'project','priority':0.9,'changefreq':'daily'},
       {'url':'homework','priority':0.9,'changefreq':'daily'},
       {'url':'physics','priority':0.9,'changefreq':'daily'},
       {'url':'chemistry','priority':0.9,'changefreq':'daily'},
       {'url':'math','priority':0.9,'changefreq':'daily'},
       {'url':'programming','priority':0.9,'changefreq':'daily'},
       {'url':'science','priority':0.9,'changefreq':'daily'},
       {'url':'english','priority':0.9,'changefreq':'daily'},
       {'url':'biology','priority':0.9,'changefreq':'daily'},
       {'url':'engineer','priority':0.9,'changefreq':'daily'},
       {'url':'management','priority':0.9,'changefreq':'daily'},
       {'url':'cs','priority':0.9,'changefreq':'daily'},
       {'url':'stats','priority':0.9,'changefreq':'daily'},
       {'url':'accounting','priority':0.9,'changefreq':'daily'},
       {'url':'eco','priority':0.9,'changefreq':'daily'},
       {'url':'nursing','priority':0.9,'changefreq':'daily'},
       {'url':'refund','priority':0.9,'changefreq':'daily'},
       {'url':'privacy','priority':0.9,'changefreq':'daily'},
       {'url':'terms','priority':0.9,'changefreq':'daily'},
       {'url':'faq','priority':0.9,'changefreq':'daily'},
       {'url':'finance','priority':0.9,'changefreq':'daily'},
       {'url':'blog','priority':0.9,'changefreq':'daily'},              
       {'url':'blog-1','priority':0.9,'changefreq':'daily'},       
       {'url':'blog-2','priority':0.9,'changefreq':'daily'},       
       {'url':'blog-3','priority':0.9,'changefreq':'daily'},       
       {'url':'blog-4','priority':0.9,'changefreq':'daily'},       
       {'url':'blog-5','priority':0.9,'changefreq':'daily'},       
       {'url':'blog-6','priority':0.9,'changefreq':'daily'},       

    ]
       
    def items(self):
        return [item['url'] for item in self.static_url_list]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return {element['url']: element['priority'] for element in self.static_url_list}[item]

    def changefreq(self, item):
        return {element['url']: element['changefreq'] for element in self.static_url_list}[item]