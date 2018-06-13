
const fs = require('fs')
const blue = require('bluebird')
const axios = require('axios')
const readFileP = blue.promisify(fs.readFile)
const data = require('../mockData/hostJob.js')
//获取首页热门职位接口
module.exports = async (ctx)=>{
    let resp = await axios.get('http://www.baidu.com')
    console.log(resp)
    ctx.response.type = 'json'
    ctx.body = {code: 200, data: data, message: 'ok'}
}
