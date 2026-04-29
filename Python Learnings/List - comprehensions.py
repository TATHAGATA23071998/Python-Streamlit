domains = ['www.google.com', ''
            'localhost', 
            'openai.com', 
            'WWW.DATAWITHBARAA.COM']

# Using list comprehension to filter and transform the domains
filtered_domains = [
                    domain.lower().replace('www.', '') 
                    for domain in domains
                    if '.' in domain
                    ]
print(filtered_domains)