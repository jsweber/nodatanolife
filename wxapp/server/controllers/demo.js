const axios = require('axios')

module.exports = async ctx=> {
    let resp = await axios.get('https://unpkg.com/axios/dist/axios.min.js')
    console.log('===============',resp.data)
    // resp = resp.charAt(1)
    ctx.response.type = 'text'
    ctx.body = resp.data
}
