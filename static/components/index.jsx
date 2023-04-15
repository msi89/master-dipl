

function App() {

    const [loading, setLoading] = React.useState(false)
    const [error, setError] = React.useState()
    const [data, setData] = React.useState()
    const [imageUrl, setImageUrl] = React.useState()
    const [status, setStatus] = React.useState()

   const uploadImage = () => {
        setLoading(true)
        const formData = new FormData()

        formData.append("image", data)

        fetch("/upload", {
            method: "post",
            body: formData
        }).then(res => res.json()).
        then(result => {
            console.log("url", result)
            setLoading(false)
            setImageUrl(result.url)
            setStatus(result.status)
            setError()
        }).catch(err => {
            setLoading(false)
            setError(err)
        })
    }

    function handleSubmit(e){
        e.preventDefault()
       uploadImage()
    }

    function selectFileChange(event) {
        setData(event.target.files[0])
        setImageUrl(URL.createObjectURL(event.target.files[0]))
        console.log(URL.createObjectURL(event.target.files[0]))
    }

    return <div className="w-screen h-screen flex flex-col justify-center items-center">
        Hello
        {!loading &&  <form encType="multipart/form-data" onSubmit={handleSubmit}>
            <input name="files" type="file"   accept="image/*" onChange={selectFileChange}/>
            {imageUrl && <button type="submit" className="bg-blue-300 text-white px-2 py-1 rounded-sm">Detect</button>}
        </form>}
        <div className={`border-2 m-3 w-[400px] h-[300px] ${loading ? "border-gray-400": status == "Sick" ? "border-red-400": "border-green-400"}`}>
            <div className="flex">
              {imageUrl && <img src={imageUrl} className="w-full h-full"/>}
            </div>
            {loading ? <div className={`text-white text-center bg-gray-400`}>Loading...</div> :
                <div className={`text-white text-center ${ status === "Sick" ? "bg-red-400": status === 'Healthy'?  "bg-green-400": "bg-gray-400"}`}>
                    { status}
                </div>
            }
        </div>
    </div>
}