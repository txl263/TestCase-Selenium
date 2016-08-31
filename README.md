# TestCase-Selenium
Selenium TestCase Wukong
### 分类  
1. specialSale  
	a. 所有对象和它们的属性（文本、数值）  
	b. 各个对象的事件（click等）
2. mainpage  
3. task  
4. userCenter  

####测试框架  
1. 控件-页面-测试用例
2. 场景片段-场景

  ![场景片段-场景](./Image/片段场景.jpg)
 
 使用XML存储每个页面元素的ID（或者class名字或者xpath路径）和属性。  
 使用XML存储每一个测试场景片段。  
 使用XML存储场景组合的测试用例。  
 
 特卖页XPath分析
 根：html/body/div[1]
 特卖产品：div class="n-top" 
    html/body/div[1]/div[x]
    产品名字：html/body/div[1]/div[x]/a/div[1]/p/span[1]
    期数：html/body/div[1]/div[X]/a/div[1]/p/span[2]
    预期年化收益率：html/body/div[1]/div[x]/a/div[3]/p
    封闭期：html/body/div[1]/div[x]/a/div[4]/p[1]/span
    起投：html/body/div[1]/div[x]/a/div[4]/p[2]/span
    限购：html/body/div[1]/div[x]/a/div[4]/p[3]/span
    马上加入：/html/body/div[1]/div[2]/div/a
    /html/body/div[1]/div[3]