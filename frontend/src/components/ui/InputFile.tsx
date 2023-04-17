
// import './style.css'

// return <div className="flex border border-dashed p-2 m-2">
//   {/* <input type="file" name="file" id="file" multiple accept="image/*" className="block bg-green-50 focus:outline-none" /> */}

//   <input type="file" name="file" id="file" className="w-[0.1px] h-[0.1px] opacity-0 overflow-hidden absolute z-[-1]" />

//   <label htmlFor="file" className="flex ">
// <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
//   <path strokeLinecap="round" strokeLinejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
// </svg>
//     Choose a file
//   </label>

// </div>

type Prop = React.DetailedHTMLProps<React.InputHTMLAttributes<HTMLInputElement>, HTMLInputElement>
function InputFile(prop: Prop) {

  return <>

    <input {...prop} type="file" className="block w-full border border-gray-200 shadow-sm rounded-md text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400
    file:bg-transparent file:border-0
    file:bg-gray-100 file:mr-4
    file:py-3 file:px-4
    dark:file:bg-gray-700 dark:file:text-gray-400"/>

    <label htmlFor={prop.id} className="sr-only">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
        <path strokeLinecap="round" strokeLinejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
      </svg>

    </label>

  </>
}


export default InputFile


