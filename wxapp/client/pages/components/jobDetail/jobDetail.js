
Component({
    properties: {
        info: {
            type: Object,
            value: {}
        }
    },
    data: {
        
    },
    methods: {
        close(){
            this.triggerEvent('close')
        },
        open(){
            this.triggerEvent('open')
        }
    }
})
