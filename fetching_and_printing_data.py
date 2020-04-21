from taking_input_and_validating_range_and_URL import input_blog_name,input_post_range,check_range_in_negative,api_parameters,check_url_validity

def fetch_json_data_from_tumblr_url(response_code):
    fetched_string_result = response_code.text[22:-2] 
    #data fetched as string  
    json_parsed_data = json.loads(fetched_string_result)  
    #data is converted into json object
    return json_parsed_data
     
def print_basic_blog_details(json_parsed_data):
  print("name:",json_parsed_data["tumblelog"]["name"])
  print("Total:",json_parsed_data["posts-total"])
  print("title:",json_parsed_data["tumblelog"]["title"])
  print("description:",json_parsed_data["tumblelog"]["description"])

def print_photo_post_urls(json_parsed_data,tumblr_post_range):
  range=tumblr_post_range.split('-')
  post_counter=int(range[0])
  for post in json_parsed_data["posts"]:
      print(str(post_counter)+". "+post["photo-url-1280"])
      if(post["photos"]==0):
        #check if multiple posts exist or not in a post
        pass
      else:
        for multiple_post in post["photos"]:
          print("   "+multiple_post["photo-url-1280"])
      post_counter+=1
      

def main():
   tumblr_blog_name = input_blog_name()   
   tumblr_post_range = input_post_range()
   tumblr_post_range = check_range_in_negative(tumblr_post_range)
   response_code = check_url_validity(tumblr_blog_name,tumblr_post_range)
   json_parsed_data = fetch_json_data_from_tumblr_url(response_code)
   print_basic_blog_details(json_parsed_data)
   print_photo_post_urls(json_parsed_data,tumblr_post_range)

main()