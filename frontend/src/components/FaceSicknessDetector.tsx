import { useEffect, useMemo, useState } from "react";
import { Spinner } from "./ui/Spinner";
import { detectAsymetry } from "../services/services";
import { AsymetryResult } from "../services/models";


type Prop = {
    src: string
    onDelete?: (src: string) => void
    onClick?: (src: string, result: AsymetryResult) => void
};

export function FaceSicknessDetector(prop: Prop) {

    const [url, setURL] = useState(prop.src)
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<AsymetryResult>();

    useEffect(() => {
        loadAsymmetry()
    }, [prop.src])

    const reformat = useMemo(() => {
        if(!result) return {class: '', status: ''}
        if(result.symmetry < 0.1) return {
            class: 'bg-red-500',
            status: 'critical'
        }
        else if(result.symmetry < 0.5) return {
            class: 'bg-orange-500',
            status: 'normal'
        }
        else return {
            class: 'bg-green-500',
            status: 'good'
        }
    }, [result])

    async function loadAsymmetry(){
        let blob = await fetch(prop.src).then(r => r.blob());
        setLoading(true)
        detectAsymetry(blob).then(res => {
          console.log(res.data);
          setURL(`http://localhost:8000/${res.data.image_url}`)
          setResult(res.data.result[0])
          setLoading(false)
        }).catch(err =>  {
          setLoading(false)
        })
    }

    return <div className="relative w-[200px] h-[200px]"  >
    <img src={url} className="w-full h-full object-cover" onClick={() => {
       if(prop.onClick) prop.onClick(url, result!)
    }}/>
    <div className="absolute top-0 p-2 cursor-pointer text-red-400 hover:text-red-600" onClick={() => {
     if(prop.onDelete) prop.onDelete(prop.src)
    }}>x</div>

    {loading && <div className="absolute top-0 bottom-0 left-0 right-0 bg-black/70">
        <Spinner/> 
    </div>}
    {result && <div className={ `text-white text-[12px] absolute bottom-0 right-0 py-1 px-2  ${reformat.class}`}>
        {reformat.status}: {Math.round(result.symmetry * 100)}%
    </div>}
  </div>


}