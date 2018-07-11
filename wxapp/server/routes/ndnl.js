/**
 * ajax 服务路由集合
 */
const router = require('koa-router')({
    prefix: '/api'
})
const controllers = require('../controllers')
const { auth: { authorizationMiddleware, validationMiddleware } } = require('../qcloud')

router.post('/test', controllers.test)

router.get('/swiper', controllers.ndnl.swiper)
router.get('/hotjob', controllers.ndnl.hotJob)
router.get('/s', controllers.ndnl.search)


module.exports = router
