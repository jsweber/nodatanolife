
let myBehavior = require('../behaviors/my-hehavior.js')

Page({
    behaviors: [myBehavior],
    data: {
        loading: false,
        minLoading: false,
        searchVal: '12',
        isShow: false,
        searchResults: [{
            id: 1,
            job_name: '前端开发工程师'
        }, {
            id: 2,
            job_name: 'java开发工程师'
        }],
        singleJobInfo: {
            id: 1,
            job_name: '前端开发工程师',
            company: '人立方',
            salary: '10万',
            descible: `我们一直用GitHub作为免费的远程仓库，如果是个人的开源项目，放到GitHub上是完全没有问题的。其实GitHub还是一个开源协作社区，通过GitHub，既可以让别人参与你的开源项目，也可以参与别人的开源项目。

            在GitHub出现以前，开源项目开源容易，但让广大人民群众参与进来比较困难，因为要参与，就要提交代码，而给每个想提交代码的群众都开一个账号那是不现实的，因此，群众也仅限于报个bug，即使能改掉bug，也只能把diff文件用邮件发过去，很不方便。
            
            但是在GitHub上，利用Git极其强大的克隆和分支功能，广大人民群众真正可以第一次自由参与各种开源项目了。
            
            如何参与一个开源项目呢？比如人气极高的bootstrap项目，这是一个非常强大的CSS框架，你可以访问它的项目主页https://github.com/twbs/bootstrap，点“Fork”就在自己的账号下克隆了一个bootstrap仓库，然后，从自己的账号下clone：`,
            required: `我们一直用GitHub作为免费的远程仓库，如果是个人的开源项目，放到GitHub上是完全没有问题的。其实GitHub还是一个开源协作社区，通过GitHub，既可以让别人参与你的开源项目，也可以参与别人的开源项目。

            在GitHub出现以前，开源项目开源容易，但让广大人民群众参与进来比较困难，因为要参与，就要提交代码，而给每个想提交代码的群众都开一个账号那是不现实的，因此，群众也仅限于报个bug，即使能改掉bug，也只能把diff文件用邮件发过去，很不方便。
            
            但是在GitHub上，利用Git极其强大的克隆和分支功能，广大人民群众真正可以第一次自由参与各种开源项目了。
            
            如何参与一个开源项目呢？比如人气极高的bootstrap项目，这是一个非常强大的CSS框架，你可以访问它的项目主页https://github.com/twbs/bootstrap，点“Fork”就在自己的账号下克隆了一个bootstrap仓库，然后，从自己的账号下clone：`
        }
    },
    search(e){
        console.log(getApp().globalData)
        this.setData({
            searchVal: e.detail.value.value,
            loading: true
        })
    },
    closeInfo(){
        this.setData({
            isShow: true
        })
    },
    openInfo(e){
        console.log(e.currentTarget.dataset.info)
        this.setData({
            isShow: false,
            singleJobInfo: e.currentTarget.dataset.info
        })
    },
    onReady(){
        let query = wx.createSelectorQuery().in(this)
        query.select('.result-list').boundingClientRect(res => {
            console.log(res.left)
        })
        query.selectViewport().scrollOffset()
        query.exec(res => {
            console.log(res[0].top, res[1].scrollTop)
            
            
        })
    },
    onMyEvent(e){
        console.log(e.detail)
    }
})
