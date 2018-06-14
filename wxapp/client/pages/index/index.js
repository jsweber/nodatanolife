var qcloud = require('../../vendor/wafer2-client-sdk/index')
var config = require('../../config')
var util = require('../../utils/util.js')

Page({
    data: {
        notices: [{
                img: 'http://img02.tooopen.com/images/20150928/tooopen_sy_143912755726.jpg',
                text: '截止2018年6月12日 数据已经超过650000条'
            },
            {
                img: 'http://img06.tooopen.com/images/20160818/tooopen_sy_175866434296.jpg',
                text: '上线啦'
            },
            {
                img: 'http://img06.tooopen.com/images/20160818/tooopen_sy_175833047715.jpg',
                text: '截止2018年6月12日 数据已经超过650000条'
            }
        ],
        jobArr: []
    },
    onLoad(){
        let self = this
        wx.request({
            url: `${config.service.host}/api/hotjob`,
            success(resp){
                console.log(resp)
                self.setData({
                    jobArr: resp.data.data.jobs
                })
            }
        })

        wx.request({
            url: `${config.service.host}/api/test`,
            method: 'POST',
            dataType: 'json',
            data: {
                data: {
                    arr:[{
                            img: 'http://img02.tooopen.com/images/20150928/tooopen_sy_143912755726.jpg',
                            text: '[截止2018年6月12日 数据已经超过650000条]'
                        },
                        {
                            img: 'http://img06.tooopen.com/images/20160818/tooopen_sy_175866434296.jpg',
                            text: '[上线啦]'
                        },
                        {
                            img: 'http://img06.tooopen.com/images/20160818/tooopen_sy_175833047715.jpg',
                            text: '[截止2018年6月12日 数据已经超过650000条]'
                        }
                    ]}
            },
            success(resp){
                resp = resp.data
                if (resp.code === 200){
                    self.setData({
                        notices: resp.data.arr
                    })
                }else {
                    
                }
            }
        })
    }
})