import { useEffect, useState } from 'react'
import { FileInput } from './components/ui/FileDropInput'
import { DetectFaceModal } from './components/DetectFaceModal'
import { FaceSicknessDetector } from './components/FaceSicknessDetector'
import { FaceSicknessDetectorPreview } from './components/FaceSicknessDetectorPreview'
import { AsymetryResult } from './services/models'

function App() {


  // const [fileImg, setImageFile] = useState<File[]>([])
  const [images, setImages] = useState<string[]>([])
  // const [selectedPhoto, setSelectedPhoto] = useState<File>()
  // const [selectedPhotoUrl, setSelectedPhotoUrl] = useState<string>()
  const [selectedFace, setSelectedFace] = useState<{
    photo: string,
    result: AsymetryResult
  }>()

  const [openModal, setOpenModal] = useState(false);


  useEffect(() => {
    // fetch("/app/health").then(res => res.json())
    // .then(data => console.log("health check", data))
    // .catch(err => console.error("error health", err))
  }, [])



  function handleFileChange(event: React.ChangeEvent<HTMLInputElement>) {
    const files = event.target.files
    if (files === null) return
    const photos = []
   // const imgs = []
    for (let i = 0; i < files.length; i++) {
      photos.push(URL.createObjectURL(files[i]))
      // imgs.push(files[i])
    }
    setImages([...images, ...photos])
   // setImageFile([...fileImg, ...imgs])
    console.log("image size", images.length);
  }

  return (<>
    <div>

      <h1 className="text-3xl font-bold  text-center py-3">
        Face sickness detector
      </h1>
      <FileInput onChange={handleFileChange} multiple accept="image/png,image/jpeg,image/webp" />

      <div className="flex flex-wrap p-2 gap-2">
        {/* {images.map(url => <div className="relative w-[200px] h-[200px]" key={url} >
          <img src={url} className="w-full h-full object-cover" onClick={() => {
            setSelectedPhotoUrl(url)
            setOpenModal(true)
          }}/>
          <div className="absolute top-0 p-2 cursor-pointer text-red-400 hover:text-red-600" onClick={() => {
            setImages(images.filter(c => c !== url))
          }}>x</div>
        </div>)} */}
        {images.map(url => <FaceSicknessDetector 
        key={url} 
        src={url} 
        onClick={(src, result) => {
          setSelectedFace({photo: src, result})
           setOpenModal(true)
        }}
        onDelete={(src) =>  setImages(images.filter(c => c !== url))}
        
        />)}
      </div>

    </div>
    {/* <DetectFaceModal
      open={openModal}
      setOpenModal={setOpenModal}
      imageUrl={selectedPhotoUrl}
      setImageUrl={setSelectedPhotoUrl}
    /> */}
     <FaceSicknessDetectorPreview
      open={openModal}
      setOpenModal={setOpenModal}
      summary={selectedFace}
    />
  </>
  )
}

export default App
