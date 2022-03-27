from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import random
import xmltodict

def Quote(name):
    balls = name
    try:
        name = name.lower()
        
        name = name.split(" ")
        
        #get rid of second period
        if name[0][-1] == ".":
            name[0] = name[0][:-1]
        if name[1][-1] == ".":
            name[1] = name[1][:-1]    
        
        if len(name) == 3:    
            if name[2][-1] == ".":
                name[2] = name[2][:-1]    
           
        #url (API) name rules
        apiName = name[0]
        nameUrl = "." + name[0].replace(".","_")
        name =  name[1:]
        
        for i in name:
            apiName += "+" + i
        
        # " " = "+"
        
        # all lower
        
        #remove second dot
        
        
        #---------------------------
        
        #url (quote) name rules
        # " " = "_"
        # id.name
        
        for i in name:
            i = i.replace(".","_")
            nameUrl += "_" + i
            
        searchName = apiName.replace("+"," ")
        
        import urllib.request    
        url = "https://www.goodreads.com/search.xml?key=ZbtYp9sJBnK097ZtJnkLQ&q={}".format(apiName)
        
    
        
        # Open the URL as Browser, not as python urllib
        page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
        infile=urllib.request.urlopen(page).read()
        data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
        page_soup = Soup(data, "html.parser") #html parsing
        
        x = xmltodict.parse(str(page_soup))
        z = x
        
    
        
        searchName = searchName.lower()
        searchName = searchName.split()
        searchName = searchName[0] + " " + searchName[-1]
            
        
        theBear = ""
        count = 0
        while theBear != searchName:
            g = z["goodreadsresponse"]["search"]["results"]["work"][count]["best_book"]["author"]["id"]["#text"]
            theBear = z["goodreadsresponse"]["search"]["results"]["work"][count]["best_book"]["author"]["name"]
            
            theBear = theBear.lower()
            theBear = theBear.split()
            theBear = theBear[0] + " " + theBear[-1]        
            
            count += 1
            
            if count == 200:
                return "not found"
            
    
        
    
    
        url = "https://www.goodreads.com/author/quotes/{}{}".format(g,nameUrl)
        
        
        try:
            # Open the URL as Browser, not as python urllib
            page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
            infile=urllib.request.urlopen(page).read()
            data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
            page_soup = Soup(data, "html.parser") #html parsing    
            
            whole = page_soup.findAll("div",{"style" : "text-align: right; width: 100%" })
            whole = whole[0].text[:-9]
            whole = whole[-2:]
            if whole[0] == " ":
                whole = whole[1]
            
        except:
            whole = 1
        
        url = "https://www.goodreads.com/author/quotes/{}{}?page={}".format(g,nameUrl,random.randint(0,int(whole)))
        
    
        # Open the URL as Browser, not as python urllib
        page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
        infile=urllib.request.urlopen(page).read()
        data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
        page_soup = Soup(data, "html.parser") #html parsing
        
        quote = page_soup.findAll("div", {"class","quoteDetails"})
        
        quote = random.choice(quote)
        
        attribute = quote.div.span.text
        quote = quote.div.text
        quote = quote.replace(attribute,"")
        quote = quote.replace("\n","")
        attribute = attribute.replace("\n","")
        attribute = attribute.replace("   ","")
        quote = quote.replace("      ","")
        quote = quote.replace("   ―  ","")
        
        if "/" in quote:
            x = quote.index("/")
            quote = quote[:x]
        
        quote = (quote.encode('ascii', 'ignore')).decode("utf-8")
            
        
        return [quote,attribute]
    except:
        return "Not found"
        
    
    #https://www.goodreads.com/search.xml?key=ZbtYp9sJBnK097ZtJnkLQ&q=Robert+Frost
    
    
    #search.authors

#__________________________________________________________________________
#Get Quotes________________________________________________________________

def getQuote(name):
    backup = name
    #lowercases it
    name = name.lower()
    #splits it into a list
    name = name.split(" ")
    
    #exceptions for people like h.p. lovecraft
    name[0] = name[0].replace(".","_")
    
    if len(name) == 3:
        name[1] = name[1].replace(".","")
    
    if name[0][-1] == "_":
        name[0] = name[0][:-1]

    #build the thing for people with all kinds of names, putting the last name first
    #[linda,lee,landon] needs to = [landon, linda, lee]
    
    urlName = name[len(name)-1]
    
    for i in range(len(name)-1):
        urlName+= "_" + name[i]
    urlInitial = urlName[0]
        
    
        
    
    try:
    
        import urllib.request    
        
        url = "http://www.notable-quotes.com/{}/{}.html".format(urlInitial,urlName)    
        
        # Open the URL as Browser, not as python urllib
        page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
        infile=urllib.request.urlopen(page).read()
        data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
        page_soup = Soup(data, "html.parser") #html parsing
        
        Whole = page_soup.findAll("p", {"class": "quotation"})
        Whole2 = page_soup.findAll("p", {"class": "attribution"})
        
        number = random.randint(0,len(Whole))
        number2 = number
        
        if len(Whole) == 0:
            Whole = page_soup.findAll("p")
            number = random.randint(0,len(Whole))           
            quote = Whole[number].text
            return[quote,backup]
        
        
        quote = Whole[number].text
        attribute = Whole2[number2].text
        
        return [quote,attribute]
    except:
        return "That author isn't listed"