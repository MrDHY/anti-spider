const puppeteer = require('puppeteer');
const redis = require("redis");
console.log('hello');

async function run() {
  const USERNAME_SELECTOR = '#create_account_email';
  const PASSWORD_SELECTOR = '#create_account_password';
  const BUTTON_SELECTOR = '#login_btn';
  // const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();

  var redis = require('redis'),
      RDS_PORT = 21601,        //端口号
      RDS_HOST = '127.0.0.1',    //服务器IP
      RDS_PWD = 'Mindata123',
      RDS_OPTS = {},            //设置项
      client = redis.createClient(RDS_PORT,RDS_HOST,RDS_OPTS);

 
  client.auth(RDS_PWD,function(){
      console.log('通过认证');
  });
   client.select("2",function(){
	  console.log("选择2")
  });


  await page.goto('https://www.itjuzi.com/user/login');
//  await page.screenshot({path: 'screenshots/itjuzi_login.png'});

  await page.waitFor(5000);

  await page.type(USERNAME_SELECTOR, "15501237820", {delay:100});

  await page.type(PASSWORD_SELECTOR, "123456", {delay:100});

  await page.click(BUTTON_SELECTOR);

  await page.waitFor(5000);
  
  await page.goto('http://radar.itjuzi.com/company');
  await page.waitFor(2000);
  
  //await page.waitForNavigation();
 // await page.screenshot({path: 'screenshots/itjuzi_first.png'});
  let cookies = await page.cookies()
  var result = {}
  for(var i=0; i < cookies.length; i++) {
    result[cookies[i].name] = cookies[i].value
    // console.log(cookies[i].name +': '+ cookies[i].value)
  }

  var cookie = result['session']
  console.log(cookie)

  client.set('cookie', cookie, redis.print);

  await page.waitFor(2000);
  client.quit()
  browser.close();
}

run();
