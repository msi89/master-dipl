import { Modal } from "./ui/Modal";
import { AsymetryResult, FaceMeasure } from "../store/models";
import { useEffect, useState } from "react";
import { getAsymetryMeasures } from "../store/services";


type Prop = {
    result?: AsymetryResult
    photo?: string
    open: boolean;
    setOpenModal: (v: boolean) => void;
  };
  const API_URL = import.meta.env.VITE_APP_API_URL
export function FaceSicknessDetectorPreview(prop: Prop) {

    const {result , photo, open, setOpenModal} = prop
    const [measures, setMeasures] = useState<FaceMeasure[]>([]);

 useEffect(() => {
  if(photo){
    getAsymetryMeasures(photo)
  .then(measures => {
   setMeasures(measures.data)
  })
  .catch(err => console.log(err))
  }
 }, [photo])
  
    return (
      <Modal
        visible={open}
        setVisible={setOpenModal}
        dismissible={false}
        name="create-car-form"
      >
        <div className="min-h-96 w-[600px]  py-4 px-[30px] text-gray-500 dark:text-gray-200 bg-white dark:bg-gray-700 shadow rounded">
          <div className="flex items-center justify-between">
            {/* <h1>Diagnostic: {result ? result.status : '' }</h1> */}
            <h1>Diagnostic</h1>
            <span onClick={() => {setOpenModal(false)}} className="cursor-pointer">x</span>
          </div>
        
          <div className="my-5 w-full relative" >
            <div className="h-[400px] w-full">
               {photo && <img src={`${API_URL}/${photo}`} className=" w-full h-full object-cover"/> }
            </div>
           
            { result && <div className="flex flex-col items-center p-4 w-full">
              <span>You face symmetry of {Math.round(result.symmetry * 100)}%</span>
              {/* <span> {result.descrition}</span> */}
            </div> }
            {measures.length  && <div className=" grid grid-cols-2">
              <div>Face height</div>
              <div className="text-right">{measures[0].face_height}</div>
              <div>Face width</div>
              <div className="text-right">{measures[0].face_width}</div>
              <div>Left eye width</div>
              <div className="text-right">{measures[0].left_eye_width}</div>
              <div>Right eye width</div>
              <div className="text-right">{measures[0].right_eye_width}</div>
              <div>Month width</div>
              <div className="text-right">{measures[0].mouth_width}</div>
              <div>Nose width</div>
              <div className="text-right">{measures[0].nose_width}</div>
              <div>Vertical asymmetry</div>
              <div className="text-right">
              {parseFloat((measures[0].vertical_asymmetry*100).toFixed(1))}%
              </div>
              <div>Horizontal asymmetry</div>
              <div className="text-right">
               {parseFloat((measures[0].horizontal_asymmetry*100).toFixed(1))}%
              </div>
              <div>Proportionality</div>
              <div className="text-right">
                {parseFloat((measures[0].proportionality*100).toFixed(1))}%
              </div>
            </div>}
          </div>

        </div>
      </Modal>
    );
  };