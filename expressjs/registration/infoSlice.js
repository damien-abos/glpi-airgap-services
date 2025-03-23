import { createSlice } from "@reduxjs/toolkit"
import data from '../data.json' with { type: 'json' }

const infoSlice = createSlice({
    name: "registrationInfo",
    initialState: data.registration.info,
    reducers: {
        infoUpdated(state, action) {
            state.push(action.payload)
        }
    }
})

export default infoSlice.reducer