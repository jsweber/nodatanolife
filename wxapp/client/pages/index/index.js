var qcloud = require('../../vendor/wafer2-client-sdk/index')
var config = require('../../config')
var util = require('../../utils/util.js')

Page({
    data: {
        swipers: [],
        jobArr: []
    },
    onLoad(){
        let self = this
        wx.request({
            url: `${config.service.host}/api/swiper`,
            success(resp){
                resp = resp.data
                console.log(resp)
                self.setData({
                    swipers: resp.data
                })
            }
        })

        wx.request({
            url: `${config.service.host}/api/hotjob`,
            method: 'GET',
            dataType: 'json',
            success(resp){
                resp = resp.data
                if (resp.code === 200){
                    self.setData({
                        jobArr: resp.data.jobs
                    })
                }else {
                    
                }
            }
        })
    }
})