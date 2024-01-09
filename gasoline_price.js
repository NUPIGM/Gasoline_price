// 引入所需的库
const axios = require("axios");
const cheerio = require("cheerio");
// 在请求中包含和保存服务端的 cookie
// axios.defaults.withCredentials = true;
// 发出 HTTP 请求以获取网页内容
url_main = "https://cx.sinopecsales.com/yjkqiantai/core/main"
url_get = "https://cx.sinopecsales.com/yjkqiantai/data/initMainData"//get
url_post = "https://cx.sinopecsales.com/yjkqiantai/data/switchProvince"//post
const axios = require('axios');

// 定义 POST 请求的数据
const postData = {
  key1: 'value1',
  key2: 'value2'
};

// 发送 POST 请求
axios.post(url_post, postData)
  .then(response => {
    console.log('Response:', response.data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
