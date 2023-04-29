import { useEffect, useMemo, useState } from "react";
import { Spinner } from "./ui/Spinner";
import { detectAsymetry, getAsymetryMeasures } from "../store/services";
import { AsymetryResult, AsymetryStatusEnum, FaceMeasure } from "../store/models";


type Prop = {
    src: string
    onDelete?: (src: string) => void
    onClick?: (src: string, result: AsymetryResult) => void
};

const API_URL = import.meta.env.VITE_APP_API_URL

export function FaceSicknessDetector(prop: Prop) {

    const [url, setURL] = useState<string>()
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<AsymetryResult>();
  

    useEffect(() => {
        loadAsymmetry()
    }, [prop.src])

    const bannerColor = useMemo(() => {
        if(!result) return ''
        switch(result.status) {
            case AsymetryStatusEnum.CRITICAL: return 'bg-red-500'
            case AsymetryStatusEnum.NONCRITICAL: return 'bg-orange-500'
            default: return 'bg-green-500'
        }
    }, [result])

    async function loadAsymmetry(){
        let blob = await fetch(prop.src).then(r => r.blob());
        setLoading(true)
        detectAsymetry(blob).then(res => {
          console.log(res.data);
           setURL(res.data.image_url)
           if(res.data.result.length)
           setResult(res.data.result[0])
          setLoading(false)
        }).catch(err =>  {
          setLoading(false)
        })
    }

 

    return <div className="relative w-[200px] h-[200px]"  >
    <img src={ url ? `${API_URL}/${url}`: prop.src} className="w-full h-full object-cover" onClick={() => {
       if(prop.onClick && url) prop.onClick(url, result!)
    }}/>
    <div className="absolute top-0 p-2 cursor-pointer text-red-400 hover:text-red-600" onClick={() => {
     if(prop.onDelete) prop.onDelete(prop.src)
    }}>x</div>

    {loading && <div className="absolute top-0 bottom-0 left-0 right-0 bg-black/70">
        <Spinner/> 
    </div>}
    {result && <div className={ `text-white text-[12px] absolute bottom-0 right-0 py-1 px-2  ${bannerColor}`}>
        {result.status}: {Math.round(result.symmetry * 100)}%
    </div>}
  </div>


}