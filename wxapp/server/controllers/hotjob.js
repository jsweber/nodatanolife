
const fs = require('fs')
const blue = require('bluebird')
const axios = require('axios')
const readFileP = blue.promisify(fs.readFile)
const data = require('../mockData/hostJob.js')
//获取首页热门职位接口
module.exports = (ctx)=>{
    ctx.response.type = 'json'
    ctx.body = {code: 200, data: data, message: 'ok'}
}
