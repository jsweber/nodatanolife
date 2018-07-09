/**
 * 如果有同名的属性或方法，组件本身的属性或方法会覆盖 behavior 中的属性或方法，如果引用了多个 behavior ，在定义段中靠后 behavior 中的属性或方法会覆盖靠前的属性或方法；
如果有同名的数据字段，如果数据是对象类型，会进行对象合并，如果是非对象类型则会进行相互覆盖；
生命周期函数不会相互覆盖，而是在对应触发时机被逐个调用。如果同一个 behavior 被一个组件多次引用，它定义的生命周期函数只会被执行一次
 */

module.exports = Behavior({
    behaviors: [],
    properties: {
        myBehaviorData: {
            type: String,
            value: 123
        }
    },
    data: {
        myData: 123
    },
    attached(){
        //behavior中的相同钩子早于components中的钩子执行
    },
    methods: {

    }
})