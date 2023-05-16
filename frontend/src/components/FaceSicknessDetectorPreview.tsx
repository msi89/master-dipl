import { Modal } from "./ui/Modal";
import { Asymetry, FaceMeasure } from "../store/models";
import { useEffect, useState } from "react";
import { getAsymetryMeasures } from "../store/services";

const API_URL = import.meta.env.VITE_APP_API_URL

type Prop = {
    data?: Asymetry
    open: boolean;
    setOpenModal: (v: boolean) => void;
  };

export function FaceSicknessDetectorPreview(prop: Prop) {

    const {data , open, setOpenModal} = prop
  
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
            <h1>Диагностика </h1>
            <span onClick={() => {setOpenModal(false)}} className="cursor-pointer">x</span>
          </div>
        
          <div className="my-5 w-full relative" >
            <div className="h-[400px] w-full">
               {<img src={`${API_URL}/${data?.image_url}`} className=" w-full h-full object-cover"/> }
            </div>
           
            { data?.result.length && <div className="flex flex-col items-center p-4 w-full">
              {/* <span>You face symmetry of {Math.round(data.result[0].symmetry * 100)}%</span> */}
              {/* <span> {result.descrition}</span> */}
            </div> }
            {  data?.measure.length  && <div className=" grid grid-cols-2 text-sm">
              <div>{/*Face height*/}Высота лица</div> 
              <div className="text-right">{data?.measure[0].face_height}</div>
              <div>{/*Face width*/}Ширина лица</div>
              <div className="text-right">{data?.measure[0].face_width}</div>
              <div>{/*Left eye width*/}Ширина левого глаза</div>
              <div className="text-right">{data?.measure[0].left_eye_width}</div>
              <div>{/*Right eye width*/}Ширина правого глаза</div>
              <div className="text-right">{data?.measure[0].right_eye_width}</div>
              <div>{/*Month width*/}Ширина рта</div>
              <div className="text-right">{data?.measure[0].mouth_width}</div>
              <div>{/*Nose width*/}Ширина носа</div>
              <div className="text-right">{data?.measure[0].nose_width}</div>
              <div>{/*Vertical asymmetry*/}Вертикальная асимметрия</div>
              <div className="text-right">
              {parseFloat((data?.measure[0].vertical_asymmetry*100).toFixed(1))}%
              </div>
              <div>{/*Horizontal asymmetry*/}Горизонтальная асимметрия</div>
              <div className="text-right">
               {parseFloat((data?.measure[0].horizontal_asymmetry*100).toFixed(1))}%
              </div>
              <div>{/*Proportionality*/}Пропорциональность</div>
              <div className="text-right">
                {parseFloat((data?.measure[0].proportionality*100).toFixed(1))}%
              </div>
            </div>}
          </div>

        </div>
      </Modal>
    );
  };