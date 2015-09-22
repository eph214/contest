from multiprocessing import Pool
import httplib2

# define your concurrency level for hammering your server
concurrencyCount=200

# define the url you want to test concurrency on
url='https://localhost'


def f(url):
    #print url
    h=httplib2.Http(disable_ssl_certificate_validation=True)
    resp, content = h.request(url,
    headers={'cache-control':'no-cache'})
    #print content
    print resp

pool = Pool(processes = concurrencyCount)
tasks=[]
for num in range(1,200):
    tasks.append(url)


print pool.map(f, tasks)
