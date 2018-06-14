const axios = require('axios')

module.exports = async ctx=> {
    let resp = await axios.get('https://nodatanolife.cn/api/test',{
        params: {data: ctx.request.body.data}
    })
    // resp = resp.charAt(1)
    ctx.response.type = 'json'
    ctx.body = resp.data
}
