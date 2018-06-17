const axios = require('axios')
const {Test} = require('../api')

module.exports = async ctx=> {
    let resp = await axios.post(Test ,{
        data: ctx.request.body.data
    })
    // resp = resp.charAt(1)
    ctx.response.type = 'json'
    try{
        resp.data.data = JSON.parse(resp.data.data)
    }catch(e){
        console.log('返回的不是json数据 或者 不需要解析')
    }
    
    ctx.body = resp.data
}
