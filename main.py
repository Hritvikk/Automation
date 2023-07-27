from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


import time
def validateSearch():  
    driver = webdriver.Chrome(executable_path="C:\\Users\\hgupta\\Downloads\\chromedriver.exe")
    driver.get("http://localhost:3000/")
    username = 'test@gmail.com'
    password = 'pass'
    searchKey = 'rick'
    # timeoutShort = 1
    # timeoutLong = 3
    time.sleep(1)
    username_field = driver.find_element(By.ID, "outlined-basic-login")
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, "outlined-basic-password")
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, "outlined-basic-click")
    login_button.click()
    time.sleep(1)
    search_field = driver.find_element(By.ID, ":r5:")
    search_field.send_keys(searchKey)
    time.sleep(2)
    all_records = []
    record_names=[]
    last=''
    while True:
        records=driver.find_elements(By.XPATH,"//div[@data-colindex='0']")
        if len(records)==0:
            break
    
        for i in records:
            all_records.append(i)
            try:
                record_names.append(i.text)
            except:
                continue
        first = record_names[-1]

        if first == last:
            break

        last = record_names[-1]
        driver.execute_script("arguments[0].scrollIntoView();", records[-1])
        time.sleep(2)


        if len(record_names)>19:
            break
    anyWrong = 0
    print(record_names)
    for name in record_names:
        if searchKey.lower() not in name.lower():
            print("Error: Wrong result present in search : {}".format(name))
            anyWrong+=1
    if anyWrong==0:
        print("All search results validated successfully!")
    else:
        print("Total errors in search : {}".format(anyWrong))
    time.sleep(2)
    search_field.send_keys('')
    return driver

def store_records(driver):
    records_name=[]
    all_records=[]
    last_ele=""
    while(True):
        
        records=driver.find_elements(By.XPATH,"//div[@data-colindex='0']")
        if len(records)==0:
            break
    
        for i in records:
            all_records.append(i)
            records_name.append(i.text)

        first_ele=records_name[-1]
        if first_ele==last_ele:
            break
        last_ele=records_name[-1]
        driver.execute_script("arguments[0].scrollIntoView();", records[-1])
        time.sleep(2)
    
    records_name=set(records_name)
    
    print(records_name)
    print(len(records_name))
    return records_name

def validate_sorted_records():

    records_name=store_records(driver)
        
    sorted_record_name=sorted(records_name)
    #store_records(driver)
    print(sorted_record_name)

def sort_ascending(driver):
    sort_list = []
    store_records(driver)
    sort_button = driver.find_element(By.XPATH, '//div/div[text()="Name"]/../../div/button[@title="Sort" and @type="button"]')
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    action = ActionChains(driver)

    while True:
        for_parent_of_last = driver.find_elements(By.XPATH, "//div[@data-rowindex = '19']")
        res = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]')
        for i in res:
            if i.text not in sort_list:
                sort_list.append(i.text)
        action.scroll_to_element(res[-1]).perform()
        if for_parent_of_last:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "19"]/div[@data-field="name"]/div[text()]')
            sort_list.append(res.text)
            break
        
    error_raised = False
    for i in range(len(sort_list)-1):
        if sort_list[i] > sort_list[i+1]:
            error_raised = True
    if not error_raised:
        print("Ascending Sort Validated!")
    else:
        print("Error: Ascending Sort Failed!")
    # print(f"sorted-list = {sort_list}")
    

def sort_descending(driver):
    sort_list = []
    store_records(driver)
    sort_button = driver.find_element(By.XPATH, '//div/div[text()="Name"]/../../div/button[@title="Sort" and @type="button"]')
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    action = ActionChains(driver)

    while True:
        for_parent_of_last = driver.find_elements(By.XPATH, "//div[@data-rowindex = '19']")
        res = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]')
        for i in res:
            if i.text not in sort_list:
                sort_list.append(i.text)
        action.scroll_to_element(res[-1]).perform()
        if for_parent_of_last:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "19"]/div[@data-field="name"]/div[text()]')
            sort_list.append(res.text)
            break
    error_raised = False
    for i in range(len(sort_list)-1):
        if sort_list[i] < sort_list[i+1]:
            error_raised = True
    if not error_raised:
        print("Descending Sort Validated!")
    else:
        print("Error: Descending Sort Failed!")
    # print(f"sorted-list = {sort_list}")
    
            


if __name__=='__main__':
    driver = validateSearch()
    sort_ascending(driver)

    sort_descending(driver)