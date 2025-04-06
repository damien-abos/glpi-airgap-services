//import data from './data.json' with { type: 'json' }
import { configureStore } from '@reduxjs/toolkit'
import reduxLogger from 'redux-logger'
import infoReducer from  './registration/infoSlice.js'
import offersReducer from './registration/offersSlice.js'
import pluginsReducer from './marketplace/pluginsSlice.js'
import tagsReducer from './marketplace/tagsSlice.js'

const logger = reduxLogger.createLogger()

const store = configureStore({
    reducer: {
        marketplacePlugins: pluginsReducer,
        marketplaceTags: tagsReducer,
        registrationInfo: infoReducer,
        registrationOffers: offersReducer
    },
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger)
})

export default store