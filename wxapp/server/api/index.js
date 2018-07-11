const {Host, Prefix} = require('./config')

module.exports = {
    Test: `${Host}${Prefix}test`,
    Search: `${Host}${Prefix}s`,
}