
let myBehavior = require('../behaviors/my-hehavior.js')

Page({
    behaviors: [myBehavior, 'wx://form-field'],
    data: {
        loading: false,
        minLoading: false,
        searchVal: '12',
        isShow: true,
        searchResults: [1, 2]
    },
    search(e){
        console.log(getApp().globalData)
        this.setData({
            searchVal: e.detail.value.value,
            loading: true
        })
    },
    closeDetail(){
        this.setData({
            isShow: true
        })
    },
    showDetail(e){
        console.log(e.currentTarget.dataset.id)
        this.setData({
            isShow: false
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
