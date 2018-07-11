const {SwiperData, HotJobData} = require('../mockData')
const axios = require('axios')
const {Test, Search} = require('../api')

function buildResp(data){
    return {
        code: 200,
        data: data,
        message: 'ok'
    }
}

function swiper(ctx){
    ctx.response.type = 'json'
    ctx.body = buildResp(SwiperData)
}

async function hotJob(ctx){
    let resp = await axios.post(Test ,{
        data: HotJobData //ctx.request.body.data
    })
    // resp = resp.charAt(1)
    // console.log(resp.data) //http body内容 { code: 200,data: { jobs: [ '前端工程师', '算法工程师', '产品经理' ] },message: 'ok' }
    ctx.response.type = 'json'
    try{
        resp.data.data = JSON.parse(resp.data.data)
    }catch(e){
        console.log('返回的不是json数据 或者 不需要解析')
    }
    
    ctx.body = resp.data
}

async function report(ctx){
    let resp = await axios.post(Test, {
        // data : 
    })
}

async function search(ctx){
    console.log(ctx.request)
    let q = '', resp = ''
    if (ctx.method === 'GET'){
        q = ctx.request.query.q 
    }
    else if (ctx.method === 'POST'){
        q = ctx.request.body.q 
    }
    // resp = await axios.post(Search, {
    //     s : ctx.require.body.q 
    // })
    ctx.body = JSON.stringify(resp)
}

module.exports = {
    swiper,
    hotJob,
    search
}
