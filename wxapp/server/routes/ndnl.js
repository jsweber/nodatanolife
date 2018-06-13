/**
 * ajax 服务路由集合
 */
const router = require('koa-router')({
    prefix: '/app'
})
const controllers = require('../controllers')
const { auth: { authorizationMiddleware, validationMiddleware } } = require('../qcloud')

router.get('/hotjob', controllers.hotjob)

module.exports = router
