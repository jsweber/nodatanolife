import * as echarts from '../../ec-canvas/echarts'

function initChart(canvas, width, height){
    const chart = echarts.init(canvas, null, {
        width: width,
        height: height
    })

    canvas.setChart(chart)

    let option = {
        title: {
            text: '职位趋势',
            left: 'center'
        },
        color: ["#37A2DA", "#67E0E3", "#9FE6B8"],
        legend: {
            data: ['A', 'B', 'C'],
            top: 50,
            left: 'center',
            backgroundColor: 'red',
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

    chart.setOption(option)
    return chart
}


Page({
    data: {
        jobId: '',
        ec: {
            onInit: initChart
        }
    },
    onLoad(options){
        this.setData({
            jobId: options.jobid
        })
    },
    onReady(){
        // Promise.all([Promise.resolve(123)]).then(arr=>{
        //     console.log(arr)
        // })
        // this.foo()
    },
    async foo(){
        let r = await Promise.resolve(1)
        console.log(r)
    }
})