import json , requests as req, xmltodict

def blog_name_and_post_range_input():
    blog_name_input = "enter the Tumblr blog name: "
    #post_range_input = "enter the range: "
    tumblr_blog_name = input(blog_name_input)
    #tumblr_post_range = input(post_range_input)
    fetch_json_data_from_tumblr_url(tumblr_blog_name)
    
def fetch_json_data_from_tumblr_url(tumblr_blog_name):
    tumblr_blog_url = "https://renu0028.tumblr.com/api/read/json" #.format(urllib.parse.urlencode(tumblr_blog_name))
    fetched_data = req.get(tumblr_blog_url)
    xml_data = fetched_data.text
    dict_data = xmltodict.parse(xml_data)
    json_data = json.dumps(dict_data)
    json_parsed_data = json.loads(json_data)
    
    print(json_parsed_data)
    
    
def main():
    blog_name_and_post_range_input()
    
main()
