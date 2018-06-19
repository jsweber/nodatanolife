import * as echarts from '../../ec-canvas/echarts'

const defaultOption = {
    title: {
        text: '职位趋势',
        left: '10px',
        textStyle: {
            color: '#000099',
            fontSize: 15,
            lineHeight: 40,
            height: 40
        }
    },
    color: ["#37A2DA", "#67E0E3", "#9FE6B8"],
    legend: {
        data: ['A', 'B', 'C'],
        top: 0,
        left: 'right',
        z: 100
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    },
    yAxis: {
        x: 'center',
        type: 'value'
    },
    series: [
        {
            name: 'A',
            type: 'line',
            smooth: true,
            data: [18, 36, 65, 30, 78, 40, 33]
        },
        {
            name: 'B',
            type: 'line',
            smooth: true,
            data: [12, 50, 51, 35, 70, 30, 20]
        },
        {
            name: 'C',
            type: 'line',
            smooth: true,
            data: [10, 30, 31, 50, 40, 20, 10]
        }
    ]
}

function chartFactory(option){
    option = Object.assign({}, defaultOption, option ? option : {})

    function initChart(canvas, width, height){
        const chart = echarts.init(canvas, null, {
            width: width,
            height: height
        })
    
        canvas.setChart(chart)
    
        chart.setOption(option)
        return chart
    }
    return initChart
}


Page({
    data: {
        jobId: '前端工程师',
        sampleNum: 0,
        sampleTime: 0,
        staDeviation: 0.12,
        trendOption: {
            onInit: chartFactory()
        },
        salaryOption: {
            onInit: chartFactory({
                title: {
                    text: '职位薪资(单位: 人名币)',
                    left: '10px',
                    textStyle: {
                        color: '#000099',
                        fontSize: 15,
                        lineHeight: 40,
                        height: 40
                    }
                },
                color: ['#FF6600'],
                legend: {
                    data: ['salary'],
                    top: 0,
                    left: 'right',
                    z: 100
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    name: 'salary',
                    data: [820, 932, 901, 934, 1290, 1330, 1320],
                    type: 'line',
                    areaStyle: {}
                }]
            })
        }
    },
    onLoad(options){
        this.setData({
            // jobId: options.jobid
        })
    },
    onReady(){

    }
})