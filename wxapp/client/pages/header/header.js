// Page({
//     data: {
//         array: [1,2,3,4,5]
//     }
// })

Component({
    properties: {
        array: {
            type: Array,
            value: [1,2,3,4,5]
        }
    },
    externalClasses: ['cust-class'],
    data: {},
    methods: {
        tapfn(){
            this.triggerEvent('childevent', {from: 'child message'}, {bubbles: false})
        }
    }
})
