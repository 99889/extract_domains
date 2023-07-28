from urllib.parse import urlparse, urljoin

def extract_domain_and_company_links(url):
    
    parsed_url = urlparse(url)

    
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    path = parsed_url.path

    
    segments = path.strip('/').split('/')
    company_link = base_url + '/' + '/'.join(segments[:-1]) + '/'

    return company_link

# Test cases
input_url_1 = "https://www.rncos.com/about-us.htm"
input_url_2 = "https://www.abcd.com/delhi/xyz/about-us"

output_1 = extract_domain_and_company_links(input_url_1)
output_2 = extract_domain_and_company_links(input_url_2)

print(output_1)  
print(output_2)  
