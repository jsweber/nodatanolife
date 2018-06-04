var qcloud = require('../../vendor/wafer2-client-sdk/index')
var config = require('../../config')
var util = require('../../utils/util.js')

let text = 'first line'
let lineArr = []
let blockIndex = [0,1,2,3]
Page({
    data: {
        block: 'block1',
        scrollTop: 300,
        text: text,
        arr: [{text: 'first'}],
        blockIndex,
        p: {name: 'Lee', age: 30},
        loading: false
    },
    getUserInfo(e){
        console.log(e.detail)
        qcloud.loginByBtn(e.detail, {
            success(code){
                console.log(code)
            }
        })
    },
    defaultTap(e){
        this.setData({
            scrollTop: this.data.scrollTop+10
        })
    },
    onReady() {
        this.videoCtx = wx.createVideoContext('myVideo')
    },
    play() {
        this.videoCtx.play()
    },
    pause() {
        this.videoCtx.pause()
    },
    addLine(){
        lineArr.push('other line')
        this.setData({
            text: text+ '\n'+lineArr.join('\n')
        })
    },
    removeLine(){
        if (lineArr.length === 0) return 
        lineArr.pop()
        this.setData({
            text: text+ '\n'+lineArr.join('\n')
        })
    },
    onShareAppMessage(){
        return {
            title: 'tradeww',
            path: '/pages/welcome/welcome'
        }
    },
    changeText(){
        let self = this
        // wx.getLocation({
        //     type: 'wgs84',
        //     success(res){
        //         self.setData({
        //             'arr[0].text' : JSON.stringify(res)
        //         })
        //     }
        // })
        wx.vibrateLong({
            success(){
                wx.showToast({
                    title: '成功'
                })
            }
        })
    },
    alter(){
        wx.showToast({
            title: JSON.stringify(getCurrentPages()),
            icon: 'success',
            duration: 2000
        })
    },
    onParentEvent(e){
        console.log(e.detail)
    },
    setLoading(){
        this.setData({
            loading: !this.data.loading
        })
    }
})