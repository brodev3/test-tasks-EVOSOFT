import requests
import json
import os

cookies = {
    'guest_id': 'v1%3A167007989858220847',
    'kdt': 'Q6rJZNgkAEfKkWL18Sj0xeJ7dKUkwZgIh8cIajbB',
    'auth_token': '72e0211badd637c3045a88176213cf286422d5b3',
    'ct0': '2e1fab897b20cfb9f12f24f642c48095026c6053e83690116903c9898754441cc2b779ca4c09e7cf11d5aabee52ec796541cfdee8eb6621ab5af5b56d06f045676880c7f5c6915d5fb3e9f40b47473f7',
    'twid': 'u%3D1552721248177868802',
    'dnt': '1',
    'lang': 'en',
    'eu_cn': '1',
    'd_prefs': 'MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw',
    'guest_id_ads': 'v1%3A167007989858220847',
    'personalization_id': '"v1_esfIYG06KXL4HLDLY4ORnw=="',
    '_ga': 'GA1.2.1429330179.1675709910',
    '_gid': 'GA1.2.2066311953.1675709910',
}

headers = {
    'authority': 'api.twitter.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-csrf-token': '2e1fab897b20cfb9f12f24f642c48095026c6053e83690116903c9898754441cc2b779ca4c09e7cf11d5aabee52ec796541cfdee8eb6621ab5af5b56d06f045676880c7f5c6915d5fb3e9f40b47473f7',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}

def getid():
    influener = input("influener@:")

    params = {
        'variables': '{"screen_name":'+f'"{influener}"'+',"withSafetyModeUserFields":true,"withSuperFollowsUserFields":true}',
        'features': '{"responsive_web_twitter_blue_verified_badge_is_enabled":true,"responsive_web_graphql_exclude_directive_enabled":false,"verified_phone_label_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
    }

    response = requests.get(
        'https://api.twitter.com/graphql/lhB3zXD3M7e-VfBkR-5A8g/UserByScreenName',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    id = json.loads(response.text)
    return id["data"]["user"]["result"]["rest_id"]


def commentname(id):
    params = {
        'variables':'{"focalTweetId":'+f'"{id}"'+',"referrer":"profile","with_rux_injections":false,"includePromotedContent":false,"withCommunity":true,"withQuickPromoteEligibilityTweetFields":false,"withBirdwatchNotes":true,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true}',
        'features': '{"responsive_web_twitter_blue_verified_badge_is_enabled":true,"responsive_web_graphql_exclude_directive_enabled":false,"verified_phone_label_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"longform_notetweets_consumption_enabled":true,"tweetypie_unmention_optimization_enabled":true,"vibe_api_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"freedom_of_speech_not_reach_appeal_label_enabled":false,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"interactive_text_enabled":true,"responsive_web_text_conversations_enabled":false,"responsive_web_enhance_cards_enabled":false}',
    }
    response = requests.get(
        'https://api.twitter.com/graphql/9Urn0VM6X5qXUa0UdFPFlg/TweetDetail',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    replys = json.loads(response.text)
    x = 1
    y = 4
    while x < y:
        txt = replys["data"]["threaded_conversation_with_injections_v2"]["instructions"][0]["entries"][x]["content"]["items"][0]["item"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"]
        if txt[0] == "@":
            print(f'https://twitter.com/{replys["data"]["threaded_conversation_with_injections_v2"]["instructions"][0]["entries"][x]["content"]["items"][0]["item"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["screen_name"]}')
        else:
            y = y + 1
        x = x + 1

def gettweettxt(id):
    params = {
        'variables': '{"userId":'+f'"{id}"'+',"count":23,"includePromotedContent":false,"withQuickPromoteEligibilityTweetFields":false,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true}',
        'features': '{"responsive_web_twitter_blue_verified_badge_is_enabled":true,"responsive_web_graphql_exclude_directive_enabled":false,"verified_phone_label_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"longform_notetweets_consumption_enabled":true,"tweetypie_unmention_optimization_enabled":true,"vibe_api_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"freedom_of_speech_not_reach_appeal_label_enabled":false,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"interactive_text_enabled":true,"responsive_web_text_conversations_enabled":false,"responsive_web_enhance_cards_enabled":false}',
    }
    response = requests.get(
        'https://api.twitter.com/graphql/CKcd91tn0Zb0oO1jHxFmxA/UserTweets',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    tweeets = json.loads(response.text)
    if len(tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"])>2:
        print(f'Pinned tweet:\n\n{tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][2]["entry"]["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"]}\n')
        commentname(tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][2]["entry"]["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["id_str"])
        print(f'{"---" * 100}\n')
        jend = 9
    lala = json.loads(params["variables"])
    j = 0
    jend = 10
    for i in range(0,int(lala["count"])):
        if j<jend:
            if tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][i]["content"]["__typename"] == "TimelineTimelineItem" and tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][i]["content"]["itemContent"]["tweetDisplayType"]=="Tweet":
                print(f'{j+1}# Tweet:\n')
                if tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][i]["content"]["itemContent"]["tweet_results"]["result"]["legacy"].get("retweeted_status_result") is not None:
                    print(f'{tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][i]["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"].split(":")[0]}:')
                    print(f'{tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][i]["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["retweeted_status_result"]["result"]["legacy"]["full_text"]}\n')
                    commentname(tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][i]["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["retweeted_status_result"]["result"]["legacy"]["id_str"])
                    print(f'{"---" * 100}\n')
                else:
                    print(f'{tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][i]["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"]}\n')
                    commentname(tweeets["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"][1]["entries"][i]["content"]["itemContent"]["tweet_results"]["result"]["rest_id"])
                    print(f'{"---" * 100}\n')
                j+=1

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
gettweettxt(getid())








