const SwiperData = [{
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
]

const HotJobData = require('./hostJob')

const ReportData = {
    job: '前端工程师',
    sampleNum: 790,
    extractTime:[Date.now()- 7 * 24 * 3600 * 1000, Date.now()],
    staDeviation: 0.12,
    data: [{
        job: '前端工程师',
        requireList: '',
        salary: '10w',
        company: '阿里巴巴',
        extractTime: Date.now(),
        pushlishTime:  Date.now(),
    }, {
        job: 'web前端工程师',
        requireList: '',
        salary: '20w',
        company: '腾讯',
        extractTime: Date.now(),
        pushlishTime:  Date.now(),
    }]
}

module.exports = {
    SwiperData,
    HotJobData
}
