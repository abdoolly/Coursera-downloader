from selenium import webdriver
import urllib.request as urlRequest

# Credentials
email = "elgenius3000@gmail.com" # your email
password = "0146522653"          # your password

# URL
# change this to your course url week you want to download its lectures
url = "https://www.coursera.org/learn/ml-foundations/home/week/3"

# Download To
# change this to the path you want to download to in your computer
download_url = "/home/elgenius/courses/machine learning spec/ml foundation/week3/"

# file name prefix to save with
filename = "week3-"

# Path To Chrome Driver
path_to_chromedriver = './chromedriver'

### Auth XPATHS ###
email_xpath = "//*[@id=\"rendered-content\"]/div/div/div/div/div[3]/div/div/div/form/div[1]/div[1]/input"
password_xpath = "//*[@id=\"rendered-content\"]/div/div/div/div/div[3]/div/div/div/form/div[1]/div[2]/input"
submit_xpath = "//*[@id=\"rendered-content\"]/div/div/div/div/div[3]/div/div/div/form/button"
video_xpath = "//*[@id=\"rendered-content\"]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/ul/span/li[1]/a"
back_xpath = "//*[@id=\"rendered-content\"]/div/div/div/div/div/div[2]/div/div/div/nav/button[1]"
############ change this path to your computer path ################

driver = webdriver.Chrome(executable_path=path_to_chromedriver)

driver.implicitly_wait(60)
driver.maximize_window()
driver.get(url)

email_field = driver.find_element_by_xpath(email_xpath)
password_field = driver.find_element_by_xpath(password_xpath)
submit_form = driver.find_element_by_xpath(submit_xpath)
email_field.clear()
password_field.clear()

email_field.send_keys(email)
password_field.send_keys(password)
submit_form.click()


###############################

# download function
def DownloadVideo(url, name):
    urlRequest.urlretrieve(url, download_url + name)


# start getting the videos arrays
main_collections = driver.find_elements_by_class_name('rc-ItemLink')
print("There is " + str(len(main_collections)) + " videos found")
course_videos_urls = []
inner_videos = []

for vid in main_collections:
    href = vid.get_attribute('href')
    if "lecture" in str(href):
        course_videos_urls.append(href)

for video_item_index in range(0, len(course_videos_urls)):
    driver.get(course_videos_urls[video_item_index])
    download_video_url = driver.find_element_by_xpath(video_xpath)
    inner_videos.append(download_video_url.get_attribute('href'))

driver.quit()

for v in inner_videos:
    print(v)

for real_video_url_index in range(0, len(inner_videos)):
    DownloadVideo(inner_videos[real_video_url_index], filename + str(real_video_url_index + 1) + ".mp4")
