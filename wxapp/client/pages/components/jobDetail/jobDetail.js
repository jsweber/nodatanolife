
Component({
    properties: {
        innerText: {
            type: String,
            value: 'default text'
        }
    },
    data: {
        someData: {}
    },
    methods: {
        doclick(){
            console.log('click')
        },
        ontap(){
            this.triggerEvent('myevent', {
                data: 'hello'
            })
        }
    }
})
