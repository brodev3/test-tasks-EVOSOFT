import os
import snscrape.modules.twitter as sntwitter

p = input("Use proxy? y/N:")
if p == "y":
    proxyip = input("IP:")
    proxyport = input("PORT:")
    proxyUSERNAME = input("USERNAME:")
    proxyPASSWORD = input("PASSWORD:")
    proxy = f"http://{proxyUSERNAME}:{proxyPASSWORD}@{proxyip}:{proxyport}"
    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy

influener  = input("influener@:")
scraper = sntwitter.TwitterProfileScraper(f'{influener}')
i = 0
for j,tweet in enumerate(scraper.get_items()):
    replyThread = False
    if i > 9:
        break
    if (tweet.rawContent.startswith("RT @") or tweet.rawContent.startswith("@")):
        continue
    if str(tweet.inReplyToUser) == f"https://twitter.com/{influener}":
        print(f"In reply to :\n https://twitter.com/{influener}/status/{tweet.inReplyToTweetId}\n")
        print(f"{i + 1}. Thread content:\n\n {tweet.rawContent}\n")
        replyThread = True
        i-=1
    else:
        print(f"{i+1}. Tweet content:\n\n {tweet.rawContent}\n")
    if replyThread == True:
            print("Комментарии относятся к первому посту в Треде (на который отвечают)")
    else:
        scrapercomment = sntwitter.TwitterSearchScraper(f'conversation_id:{tweet.id} filter:safe')
        for c, ctweet in enumerate(scrapercomment.get_items()):
            if c > 2:
                break
            print(f"{ctweet.user}")

    print(f'{"---" * 100}\n')
    i+=1

