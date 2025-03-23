import { createSlice } from "@reduxjs/toolkit"
import data from '../data.json' with { type: 'json' }

const tagsSlice = createSlice({
    name: "marketplaceTags",
    initialState: data.marketplace.tags,
    reducers: {}
})

export default tagsSlice.reducer