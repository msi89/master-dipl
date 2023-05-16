import { useEffect, useMemo, useState } from "react";
import { Spinner } from "./ui/Spinner";
import { detectAsymetry } from "../store/services";
import { Asymetry, AsymetryResult, AsymetryStatusEnum, FaceMeasure } from "../store/models";


type Prop = {
    src: string
    onDelete?: (src: string) => void
    onClick?: (data: Asymetry) => void
};

const API_URL = import.meta.env.VITE_APP_API_URL

export function FaceSicknessDetector(prop: Prop) {

    const [loading, setLoading] = useState(false);
    const [data, setData] = useState<Asymetry>();
  

    useEffect(() => {
        loadAsymmetry()
    }, [prop.src])

    const bannerColor = useMemo(() => {
        if(!data) return ''
        if(!data.result.length) return ''
        switch(data.result[0].status) {
            case AsymetryStatusEnum.CRITICAL: return 'bg-red-500'
            case AsymetryStatusEnum.NONCRITICAL: return 'bg-orange-500'
            default: return 'bg-green-500'
        }
    }, [data])

    async function loadAsymmetry(){
        let blob = await fetch(prop.src).then(r => r.blob());
        setLoading(true)
        detectAsymetry(blob).then(res => {
          console.log(res.data);
          setData(res.data)
          setLoading(false)
        }).catch(err =>  {
          setLoading(false)
        })
    }

    return <div className="relative w-[200px] h-[200px]"  >
    <img src={ data ? `${API_URL}/${data.image_url}`: prop.src} className="w-full h-full object-cover" onClick={() => {
       if(prop.onClick && data ) prop.onClick(data)
    }}/>
    <div className="absolute top-0 p-2 cursor-pointer text-red-400 hover:text-red-600" onClick={() => {
     if(prop.onDelete) prop.onDelete(prop.src)
    }}>x</div>

    {loading && <div className="absolute top-0 bottom-0 left-0 right-0 bg-black/70">
        <Spinner/> 
    </div>}
    {/* {data && data.result.length && <div className={ `text-white text-[12px] absolute bottom-0 right-0 py-1 px-2  ${bannerColor}`}>
        {data.result[0].status}: {Math.round(data.result[0].symmetry * 100)}%
    </div>} */}
  </div>


}