import { createContext } from "react";

const resultContext = createContext({
    images: {},
    setImages: (images: any) => {},
});

export default resultContext;