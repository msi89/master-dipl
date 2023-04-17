import { Modal } from "./ui/Modal";
import { AsymetryResult } from "../services/models";


type Prop = {
    summary?: {
      photo: string,
      result: AsymetryResult
    }
    open: boolean;
    setOpenModal: (v: boolean) => void;
  };

export function FaceSicknessDetectorPreview(prop: Prop) {

    const {summary , open, setOpenModal} = prop
  
    return (
      <Modal
        visible={open}
        setVisible={setOpenModal}
        dismissible={false}
        name="create-car-form"
      >
        <div className="min-h-96 w-[600px]  py-4 px-[30px] text-gray-500 dark:text-gray-200 bg-white dark:bg-gray-700 shadow rounded">
          <div className="flex items-center justify-between">
            <h1>Diagnostic: {summary ? summary.result.status : '' }</h1>
            <span onClick={() => {setOpenModal(false)}} className="cursor-pointer">x</span>
          </div>
        
          <div className="my-5 w-full relative" >
            <div className="h-[500px] w-full">
               {summary && <img src={summary.photo} className=" w-full h-full object-cover"/> }
            </div>
           
            { summary && <div className="flex flex-col items-center p-4 w-full">
              <span>You face symmetry of {Math.round(summary.result.symmetry * 100)}%</span>
              <span> {summary.result.descrition}</span>
            </div> }
          </div>

        </div>
      </Modal>
    );
  };