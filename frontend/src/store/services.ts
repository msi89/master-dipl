import axios, { AxiosResponse } from "axios";
import { Asymetry } from "./models";

const api = axios.create({
    baseURL: import.meta.env.VITE_APP_API_URL
})

export async function detectAsymetry(file: Blob) : Promise<AxiosResponse<Asymetry, any>>{
    const form = new FormData()
    form.append("file", file)
    const c = await api.post("/detect",  form)
    return c
}