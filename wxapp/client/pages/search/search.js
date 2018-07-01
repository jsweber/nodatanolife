
Page({
    data: {
        loading: false,
        minLoading: false,
        searchVal: '12',
        isShow: true,
        searchResults: [1, 2]
    },
    search(e){
        console.log(e.detail)
        this.setData({
            searchVal: e.detail.value.value,
            loading: true
        })
    },
    closeDetail(){
        this.setData({
            isShow: true
        })
    },
    showDetail(e){
        console.log(e.currentTarget.dataset.id)
        this.setData({
            isShow: false
        })
    }
})
