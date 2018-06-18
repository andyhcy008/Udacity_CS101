
# procedure of get next target
def get_next_target(page):
    start_link = page.find('<a href=>')
	if start_link == -1:
	    return None, 0
	start_quato = page.find('"', start_link)
	end_quato = page.find('"', start_quato + 1)
	url = page[start_quato + 1 : end_quato]
	return url, end_quato
	
# procedure of print all links on page	
#def print_all_links(page):
#    while True:
#	    url, endpos = get_next_target(page)
#		if url:
#		    print url
#			page = page[endpos:]
#		else:
#		    break

# procedure of get all links as a list
def get_all_links(page):
    links = []
	while True:
	    url, endpos = get_next_target(page)
	    if url:
                links = links.append(url)
	        page = page[end_pos:]
            else:
		break
    return links

			
# *************Procedure of the combination of two procedures above  *********
def get_links(page):
    links = []
	while True:
	    end_pos = 0
            start_link = page.find('<a href=>', end_pos)
	    if start_link == -1
		    return None, 0
		else:
		    start_quato = page.find('"', start_link)
	        end_quato = page.find('"', start_quato + 1)
	        url = page[start_quato + 1 : end_quato]
		links = link.append(url)
		end_pos = end_pos + end_quato
                page = [endpos:]
	return links		
#******************************************************************************
	
             		

links = get_all_links(get_page('http://www.udacity.com/cs101x/index.html'))
print links
