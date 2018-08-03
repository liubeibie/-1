# -*- coding: utf-8 -*-


from selenium import webdriver

from PIL import Image, ImageEnhance

import pytesseract

screenImg = "E:\python项目/screenImg.png"

loginurl = "https://auto.51autogo.com:448/crm-admin/captcha"

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://auto.51autogo.com:448/crm-admin/login.jsp#")

driver.find_element_by_name("username").send_keys("15129180359")

driver.find_element_by_name("password").send_keys("Lbb123456")

# 验证码处理


driver.save_screenshot(r"E:\aa.png")

location = driver.find_element_by_id("kaptchaImage").location

size = driver.find_element_by_id("kaptchaImage").size

left = location['x']

top = location['y']

right = location['x'] + size['width']

bottom = location['y'] = size['height']

# 从文件读取截图，截取验证码位置再次保存

img = Image.open(r"E:\aa.png").crop((left, top, right, bottom))

img = img.convert('L')  # 转换模式：L | RGB

img = ImageEnhance.Contrast(img)  # 增强对比度

img = img.enhance(2.0)  # 增加饱和度

img.save(img)

# 再次读取识别验证码

img = Image.open(r"E:\aa.png")

code = pytesseract.image_to_string(img)

# code= pytesser.image_file_to_string(screenImg)

#

driver.find_element_by_name("capText").send_keys(code.strip())

# driver.find_element_by_name("capText").send_keys("IlXbPk4Q8FRNXurPd2onqQ==")

driver.find_element_by_xpath("//html/body/div/div/form/div[5]/a").click()

driver.close()

driver.quit()



