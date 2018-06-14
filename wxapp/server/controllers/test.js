const axios = require('axios')

module.exports = async ctx=> {
    let resp = await axios.get('https://nodatanolife.cn/api/test',{
        params: {data: ctx.request.body.data}
    })
    // resp = resp.charAt(1)
    ctx.response.type = 'json'
    try{
        resp.data.data = JSON.parse(resp.data.data)
    }catch(e){
        console.log('返回的不是json数据')
    }
    
    ctx.body = resp.data
}
