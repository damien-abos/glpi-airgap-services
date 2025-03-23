import { createSlice } from "@reduxjs/toolkit"
import data from '../data.json' with { type: 'json' }

const offersSlice = createSlice({
    name: "registrationOffers",
    initialState: data.registration.offers,
    reducers: {
        offerUpdated(state, action) {
            state.push(action.payload)
        }
    }
})

export default offersSlice.reducer