'use client'

import { useState } from "react";
import ResultContext from "./resultContext";

const ResultState = (props: any) => {

    const [images, setImages] = useState({ original: [], generated: [] });

    return (
        <ResultContext.Provider value={{ images, setImages }}>
            {props.children}
        </ResultContext.Provider>
    )
}

export default ResultState