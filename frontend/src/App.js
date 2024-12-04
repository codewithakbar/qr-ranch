import { useEffect, useState } from "react";
import { MyClass } from "./output-medical-ssv";
import { MyClass2 } from "./output-react-ssv-kode";
import {BrowserRouter , Route, Routes , useNavigate} from 'react-router'

function App() {

  const navigate = useNavigate()
  const code = 8326
  const [inputValue, setInputValue] = useState(null)
  const [status, setStatus] = useState(false)

  const Next = () => {
    if (code == inputValue) {
      setStatus(true);
    } else {
      setStatus(false);
    }
  };


  useEffect(() => {
    navigate('/form/sick-leave/6729f4f39559136ce648474e')
  }, [])


  return (
    <>
      {/* {
        status ? (<MyClass />) : (<MyClass2 setInputValue={setInputValue} Next={Next} />)
      } */}
        <Routes>
          <Route path="/form/sick-leave/6729f4f39559136ce648474e" element={status ? (<MyClass />) : (<MyClass2 setInputValue={setInputValue} Next={Next} />)}/>
        </Routes>
    </>
  );
}

export default App;
