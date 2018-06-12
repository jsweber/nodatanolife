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
        jobArr: ['前端工程师', '算法工程师', '产品经理','前端工程师', '算法工程师', '产品经理','前端工程师', '算法工程师', '产品经理']
    }
})