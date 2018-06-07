
var qcloud = require('../../vendor/wafer2-client-sdk/index')
var config = require('../../config')
var util = require('../../utils/util.js')

Page({
    data: {
        loading: false,
        isLogined: false,
        avatar: '',
        nickname: ''
    },
    onReady(){
        let self = this
        wx.checkSession({
            success(){
                console.log('登陆状态')
                self.setData({
                    isLogined: true
                })
                self.setUserInfo(qcloud.getUserInfo())
            },
            fail(){
                console.log('未登陆状态')
                qcloud.clearSession()
            },
            complete(){
                console.log('检查是否登陆完毕')
            }
        })
    },
    formSubmit(e){
        console.log(e.detail.value)
        util.showSuccess(JSON.stringify(e.detail.value))
    },
    formReset(){
        console.log('submit reset')
    },
    getUserInfo(e){
        let self = this
        self.setData({
            loading: true
        })
        
        qcloud.loginByBtn(e.detail, {
            success(userInfo){
                self.setData({
                    loading: false,
                    isLogined: true
                })
                self.setUserInfo(qcloud.getUserInfo())
            }
        })
    },
    setUserInfo(userInfo){
        if (!userInfo) return
        console.log(userInfo)
        this.setData({
            avatar: userInfo.avatarUrl,
            nickname: userInfo.nickName
        })

    }
})
