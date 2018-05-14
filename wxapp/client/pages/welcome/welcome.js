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
        p: {name: 'Lee', age: 30}
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
        wx.getLocation({
            type: 'wgs84',
            success(res){
                self.setData({
                    'arr[0].text' : JSON.stringify(res)
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
    }
})