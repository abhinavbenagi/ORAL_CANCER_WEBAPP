import { createContext } from "react";

const resultContext = createContext({
    images: { original: [], generated: [] },
    setImages: (images: any) => { },
});

export default resultContext;