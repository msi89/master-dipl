import { useEffect, useState } from 'react'
import { FileInput } from './components/ui/FileInput'
import { FaceSicknessDetector } from './components/FaceSicknessDetector'
import { FaceSicknessDetectorPreview } from './components/FaceSicknessDetectorPreview'
import { AsymetryResult } from './store/models'


console.log("gg", import.meta.env.VITE_APP_API_URL);

function App() {

  const [images, setImages] = useState<string[]>([])
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
    for (let i = 0; i < files.length; i++) {
      photos.push(URL.createObjectURL(files[i]))
    }
    setImages([...images, ...photos])
  }

  return (<>
    <div>

      <h1 className="text-3xl font-bold  text-center py-3">
        Face sickness detector
      </h1>
      <FileInput onChange={handleFileChange} multiple accept="image/png,image/jpeg,image/webp" />

      <div className="flex flex-wrap p-2 gap-2">
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
     <FaceSicknessDetectorPreview
      open={openModal}
      setOpenModal={setOpenModal}
      summary={selectedFace}
    />
  </>
  )
}

export default App
