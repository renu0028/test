import json , requests as req,sys

def input_blog_name():
    blog_name = "enter the Tumblr blog name: "
    tumblr_blog_name = input(blog_name)
    return tumblr_blog_name

def input_post_range():
  post_range = "enter the range: "
  return input(post_range)

def check_range_in_negative(tumblr_post_range):
  if tumblr_post_range[0].isdigit():
    return tumblr_post_range
  else:
    print("Please check range provided. No posts available for negative range.")
    sys.exit()

def api_parameters(tumblr_post_range):
    range=tumblr_post_range.split('-')
    #fetching the upper and lower bound for posts
    #num_of_posts = int(range[1])-int(range[0]) + 1   
    api_param = {
    'type':'photo',
    'num':int(range[1])-int(range[0]) + 1,
    'start':int(range[0])-1
    }
    return api_param

def check_url_validity(tumblr_blog_name,tumblr_post_range):
    tumblr_blog_url = "https://"+tumblr_blog_name+".tumblr.com/api/read/json/"
    api_param=api_parameters(tumblr_post_range)
    response_code = req.get(tumblr_blog_url,api_param)
    if response_code.status_code !=200:
      print("No such tumblr blog exists!!")
      sys.exit()
    return response_code