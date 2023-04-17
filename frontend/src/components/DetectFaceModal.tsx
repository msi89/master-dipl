import { useState } from "react";
import { Modal } from "./ui/Modal";
import axios from "axios";
import { detectAsymetry } from "../services/services";
import { Spinner } from "./ui/Spinner";
import { AsymetryResult } from "../services/models";


type Prop = {
    image?: any
    imageUrl?: string
    setImageUrl?: (v: string) => void;
    open: boolean;
    setOpenModal: (v: boolean) => void;
  };

export function DetectFaceModal(prop: Prop) {

    const {imageUrl, setImageUrl , open, setOpenModal} = prop
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState();
    const [result, setResult] = useState<AsymetryResult>();


    async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
      e.preventDefault()
      if(!imageUrl) return
      let blob = await fetch(imageUrl).then(r => r.blob());
      setLoading(true)
      detectAsymetry(blob).then(res => {
        console.log(res.data);
        setResult(res.data.result[0])
        if(setImageUrl)
          setImageUrl(`http://localhost:8000/${res.data.image_url}`)
        setLoading(false)
      }).catch(err =>  {
        setLoading(false)
        setError(err)
      })

      // setTimeout(() => {
      //   setLoading(false)
      // }, 3000);
    
    }
  
    return (
      <Modal
        visible={open}
        setVisible={setOpenModal}
        dismissible={false}
        name="create-car-form"
      >
        <div className="min-h-96 w-[600px]  py-4 px-[30px] text-gray-500 dark:text-gray-200 bg-white dark:bg-gray-700 shadow rounded">
          <div className="flex items-center justify-between">
            <h1>Face sickness detection</h1>
            <span onClick={() => {setOpenModal(false)}} className="cursor-pointer">x</span>
          </div>
        
          <form className="my-5 w-full relative" onSubmit={handleSubmit}>

           

            <div className="h-[400px] w-full">
               {imageUrl && <img src={imageUrl} className=" w-full h-full object-cover"/> }
            </div>
           
            {loading ?  <div className="absolute top-0 bottom-0 left-0 right-0 bg-black/70">
               <Spinner/> 
            </div> : result ? <div className="flex flex-col items-center p-4 w-full">
              <h1>Diagnostic</h1>
              <span>symmetry: {Math.round(result.symmetry * 100)}%</span>
              <span> description: {result.descrition}</span>
            </div> :
            <button type="submit" className="w-full bg-sky-600 hover:bg-sky-700 text-center p-4 cursor-pointer " disabled={loading}>
               Start detection 
            </button>}
  
          </form>

        </div>
      </Modal>
    );
  };