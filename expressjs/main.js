import express from 'express'
import serveStatic from 'serve-static'

import store from './store.js'

const port = normalizePort(process.env.NODE_PORT || 3000)
const app = express()

app.get('/status', (req, res) => {
    res.send({ "status": "up" })
})

app.get('/api/registration/info', (req, res) => {
    res.send(store.getState().registrationInfo)
})

app.put('/api/registration/info', (req, res) => {
    store.dispatch()
    res.send(store.getState().registrationInfo)
})

app.get('/api/registration/offers', (req, res) => {
    res.send(store.getState().registrationOffers)
})

app.get('/api/marketplace/plugins', (req, res) => {
    res.send(store.getState().marketplacePlugins)
})

app.get('/api/marketplace/tags/top', (req, res) => {
    res.send(store.getState().marketplaceTags.top)
})

app.use(serveStatic('static', {}))

app.listen(port, () => {
    console.log(`listening on port ${port}`)
})

function normalizePort(val) {
    var port = parseInt(val, 10);
    if (isNaN(port)) {
        // named pipe
        return val;
    }
    if (port >= 0) {
        // port number
        return port;
    }
    return false;
}