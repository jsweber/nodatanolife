
let myBehavior = require('../behaviors/my-hehavior.js')

Page({
    behaviors: [myBehavior],
    data: {
        loading: false,
        minLoading: false,
        searchVal: '12',
        isShow: true,
        searchResults: [{
            id: 1,
            job_name: '前端开发工程师'
        }, {
            id: 2,
            job_name: 'java开发工程师'
        }],
        singleJobInfo: {}
    },
    search(e){
        console.log(getApp().globalData)
        this.setData({
            searchVal: e.detail.value.value,
            loading: true
        })
    },
    closeInfo(){
        this.setData({
            isShow: true
        })
    },
    openInfo(e){
        console.log(e.currentTarget.dataset.info)
        this.setData({
            isShow: false,
            singleJobInfo: e.currentTarget.dataset.info
        })
    },
    onReady(){
        let query = wx.createSelectorQuery().in(this)
        query.select('.result-list').boundingClientRect(res => {
            console.log(res.left)
        })
        query.selectViewport().scrollOffset()
        query.exec(res => {
            console.log(res[0].top, res[1].scrollTop)
            
            
        })
    },
    onMyEvent(e){
        console.log(e.detail)
    }
})
