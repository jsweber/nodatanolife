
Page({
    data: {
        loading: false,
        minLoading: false,
        searchVal: ''
    },
    search(e){
        console.log(e.detail)
        this.setData({
            searchVal: e.detail.value.value,
            loading: true
        })
    }
})
