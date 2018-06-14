const axios = require('axios')

module.exports = async ctx=> {
    // resp = resp.charAt(1)
    ctx.response.type = 'text'
    ctx.body = resp.data
}
