//app.js
var qcloud = require('./vendor/wafer2-client-sdk/index')
var config = require('./config')

App({
    globalData:'I am global',
    onLaunch: function () {
        qcloud.setLoginUrl(config.service.loginUrl)
    }
})