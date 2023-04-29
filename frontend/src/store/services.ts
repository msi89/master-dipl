import axios, { AxiosResponse } from "axios";
import { Asymetry, FaceMeasure } from "./models";

const api = axios.create({
    baseURL: import.meta.env.VITE_APP_API_URL
})

export async function detectAsymetry(file: Blob) : Promise<AxiosResponse<Asymetry, any>>{
    const form = new FormData()
    form.append("file", file)
    const c = await api.post("/asymmetry",  form)
    return c
}

export async function getAsymetryMeasures(file_path: string) : Promise<AxiosResponse<FaceMeasure[], any>>{
     const form = new FormData()
    form.append("file_path", file_path)
    const c = await api.post("/asymmetry/measures", form)
    return c
}