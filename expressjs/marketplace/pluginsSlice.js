import { createSlice } from "@reduxjs/toolkit"
import data from '../data.json' with { type: 'json' }

const pluginsSlice = createSlice({
    name: "marketplacePlugins",
    initialState: data.marketplace.plugins,
    reducers: {}
})

export default pluginsSlice.reducer